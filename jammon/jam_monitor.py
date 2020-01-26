import http
import ujson
import utime
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


def check_jams(display):
    for route in routes:
        start_time = route['start_time']
        stop_time = route['stop_time']
        interval = route['interval']

        global _last_check_time

        if not is_time_to_check(start_time, stop_time, interval):
            continue

        _last_check_time = utime.localtime()
        display.fill(0)
        expected_dur = int(route['expected_dur'])
        actual_dur = get_duration_in_traffic(route['origins'], route['destinations'])
        dif = actual_dur - expected_dur
        if dif > 0:
            minutes = dif / 60
            line_cnt = math.ceil(minutes / 5)
            for i in range(line_cnt):
                display.line(0, 7 - i, 7, 7 - i, 1)
                display.show()


def is_time_to_check(start_time, stop_time, interval):
    start_time_ = make_time(start_time)
    stop_time_ = make_time(stop_time)
    localtime = utime.localtime()

    if start_time_ <= localtime <= stop_time_:
        if _last_check_time is None:
            return True
        else:
            return time_.add_seconds(_last_check_time, interval) < localtime
    else:
        return False


def make_time(str_time):
    time = str_time.split(':')
    hh_ = int(time[0])
    mi_ = int(time[1])
    yy, mm, dd, hh, mi, ss, wd, dy = utime.localtime()
    return yy, mm, dd, hh_, mi_, ss, wd, dy


def get_duration_in_traffic(origins, destinations):
    url = 'maps/api/distancematrix/json?origins=' + origins + '&destinations=' + destinations + '&mode=driving&departure_time=now&language=en-US&key=' + api_key
    api_resp = http.get('maps.googleapis.com', url)
    resp_json = ujson.loads(api_resp)
    if len(resp_json['rows']) > 0:
        return resp_json['rows'][0]['elements'][0]['duration_in_traffic']['value']
