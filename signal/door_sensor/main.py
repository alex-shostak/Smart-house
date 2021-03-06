import utime
import http
import log
import led
import wifi
import time_
import sensor


log.remove()
wifi.connect()
led.blink(1)
wifi.disable_ap()
led.blink(1)
time_.set_time()
led.blink(1)


def loop():
    log.append('starting main loop')
    while True:
        try:
            if sensor.is_time_to_check_mode():
                mode = get_mode()
                sensor.set_mode(mode)
            if sensor.is_sleep_mode():
                continue
            if sensor.door_opened():
                if send_event('door_open'):
                    sensor.set_sleep_mode()
            utime.sleep(1)
        except Exception as e:
            log.write("loop: " + str(e))
            led.blink(1, 1)


def get_mode():
    return http.get('get_mode?log_activity=true')


def send_event(name):
    return http.get('save_event?name=' + name) == 'OK'


loop()