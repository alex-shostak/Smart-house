import http
import ujson
import utime
from utime import sleep
import math
import time_


def read_conf():
    with open('jam_mon_config.json', 'r') as f:
        config = ujson.loads(f.read())
    global api_key
    api_key = config['apiKey']
    global routes
    routes = config['routes']


_last_check_time = None


def check_jams(disp):
    stand_by = True
    for route in routes:
        start_time = route['start_time']
        stop_time = route['stop_time']
        interval = route['interval']

        localtime = utime.localtime()
        if not is_working_period(start_time, stop_time, localtime):
            continue

        global _last_check_time
        stand_by = False
        if not is_time_to_check(interval, localtime):
            blink(disp)
            continue

        _last_check_time = utime.localtime()
        disp.fill(0)
        expected_dur = int(route['expected_dur'])
        actual_dur = get_dur_in_traff(route['origins'], route['destinations'])
        dif = actual_dur - expected_dur
        lvl = math.ceil((dif / 60) / 5) if dif > 0 else 1
        indicator = route['indicator']
        for i in range(lvl):
            y = 0 if indicator == 't' else 7
            disp.pixel(i, y, 1)
        disp.show()
    if stand_by:
        disp.fill(0)
        disp.show()


def is_working_period(start_time, stop_time, localtime):
    start_time_ = make_time(start_time)
    stop_time_ = make_time(stop_time)
    return start_time_ <= localtime <= stop_time_


def is_time_to_check(interval, localtime):
    if _last_check_time is None:
        return True
    else:
        return time_.add_seconds(_last_check_time, interval) < localtime


def make_time(str_time):
    time = str_time.split(':')
    hh_ = int(time[0])
    mi_ = int(time[1])
    yy, mm, dd, hh, mi, ss, wd, dy = utime.localtime()
    return yy, mm, dd, hh_, mi_, ss, wd, dy


def get_dur_in_traff(origins, destinations):
    url = 'maps/api/distancematrix/json?origins=' + origins + '&destinations=' + destinations + '&mode=driving&departure_time=now&language=en-US&key=' + api_key
    api_resp = http.get('maps.googleapis.com', url)
    resp_json = ujson.loads(api_resp)
    if len(resp_json['rows']) > 0:
        return resp_json['rows'][0]['elements'][0]['duration_in_traffic']['value']


def blink(disp):
    disp.brightness(0)
    sleep(0.2)
    disp.brightness(1)
    sleep(0.2)
    disp.brightness(2)
    sleep(0.1)
    disp.brightness(3)
    sleep(0.1)
    disp.brightness(4)
    sleep(0.6)