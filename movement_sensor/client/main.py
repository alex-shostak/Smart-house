import utime
import log
import led
import wifi
import movement_sensor
import time_


class Main(object):
    def __init__(self):
        log.remove()
        wifi.connect()
        led.blink(1)
        wifi.disable_ap()
        led.blink(1)
        time_.set_time()
        led.blink(1)
        self._last_mode_check_time = utime.localtime()

    def loop(self):
        log.append('starting main loop')
        while True:
            try:
                if self._is_time_to_check_mode():
                    movement_sensor.is_sleep_mode = self._get_mode() == "SLEEP"
                    self._last_mode_check_time = utime.localtime()
                if movement_sensor.is_sleep_mode:
                    continue
                if movement_sensor.movement_detected():
                    movement_sensor.save_data()
                if movement_sensor.data_exists():
                    self._send_data()
                    movement_sensor.delete_data()
                    movement_sensor.is_sleep_mode = True
                utime.sleep(1)
            except Exception as e:
                log.write("Main.loop: " + str(e))
                led.blink(1, 1)

    def _get_mode(self):
        pass

    def _is_time_to_check_mode(self):
        return utime.localtime() > time_.add_seconds(self._last_mode_check_time, 20)

    def _send_data(self):
        pass


Main().loop()
