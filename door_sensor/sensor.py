import utime
import config
from machine import Pin
import time_


class Mode:
    SLEEP = "S"
    ACTIVE = "A"


_pin = Pin(config.GPIO.sensor_pin, Pin.IN, Pin.PULL_UP)
_mode = Mode.SLEEP
_last_mode_check_time = utime.localtime()


def is_time_to_check_mode():
    return utime.localtime() > time_.add_seconds(_last_mode_check_time, 20)


def is_sleep_mode():
    return _mode == Mode.SLEEP


def set_sleep_mode():
    set_mode(Mode.SLEEP)


def set_mode(mode):
    global _last_mode_check_time, _mode
    _mode = mode
    _last_mode_check_time = utime.localtime()


def door_opened():
    return _pin.value() == 1

