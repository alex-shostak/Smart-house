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
                #sensor.save_data()
                send_data(time_.get_time())
            #data = sensor.get_data()
            #if data:
                #pass
                #log.write(data)
                #send_data(data)
                #sensor.delete_data()
                #sensor.set_mode(sensor.Mode.SLEEP)
            utime.sleep(1)
        except Exception as e:
            log.write("loop: " + str(e))
            led.blink(1, 1)


def get_mode():
    return http.get('get_mode?log_activity=true')


def send_data(data):
    http.get('post_data?data=' + data)


loop()