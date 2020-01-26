import http
import ujson
import utime
import math


def read_conf():
    with open('jam_mon_config.json', 'r') as f:
        config = ujson.loads(f.read())
    global api_key
    api_key = config['apiKey']
    global routes
    routes = config['routes']


def check_jams(display):
    for route in routes:
        is_time_to_check = False
        if not is_time_to_check:
            continue

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


def get_duration_in_traffic(origins, destinations):
    url = 'maps/api/distancematrix/json?origins=' + origins + '&destinations=' + destinations + '&mode=driving&departure_time=now&language=en-US&key=' + api_key
    api_resp = http.get('maps.googleapis.com', url)
    resp_json = ujson.loads(api_resp)
    if len(resp_json['rows']) > 0:
        return resp_json['rows'][0]['elements'][0]['duration_in_traffic']['value']
