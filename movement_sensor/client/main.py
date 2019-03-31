import utime
import log
import led
import wifi
import movement_sensor
import time_


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
            if movement_sensor.is_time_to_check_mode():
                mode = get_mode()
                movement_sensor.set_mode(mode)
            if movement_sensor.is_sleep_mode():
                continue
            if movement_sensor.movement_detected():
                movement_sensor.save_data()
            if movement_sensor.data_exists():
                send_data()
                movement_sensor.delete_data()
                movement_sensor.set_mode(movement_sensor.Mode.SLEEP)
            utime.sleep(1)
        except Exception as e:
            log.write("loop: " + str(e))
            led.blink(1, 1)


def get_mode():
    pass


def send_data():
    pass


loop()

