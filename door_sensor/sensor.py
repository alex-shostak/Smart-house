import os
import utime
import config
from machine import Pin
import time_


class Mode:
    SLEEP = "S"
    ACTIVE = "A"


sensor_data_folder = 'sensor_data'
sensor_data_file = sensor_data_folder + '/movement.txt'
try:
    os.mkdir(sensor_data_folder)
except:
    pass

_pin = Pin(config.GPIO.sensor_pin, Pin.IN, Pin.PULL_UP)
_mode = Mode.SLEEP
_last_mode_check_time = utime.localtime()


def is_time_to_check_mode():
    return utime.localtime() > time_.add_seconds(_last_mode_check_time, 20)


def is_sleep_mode():
    return _mode == Mode.SLEEP


def set_mode(mode):
    global _last_mode_check_time, _mode
    _last_mode_check_time = utime.localtime()
    _mode = mode


def door_opened():
    return _pin.value() == 1


def save_data():
    with open(sensor_data_file, 'w') as f:
        print(time_.get_time(), file=f)


def delete_data():
    with open(sensor_data_file, 'w'):
        pass


def data_exists():
    return os.path.isfile(sensor_data_file) and os.path.getsize(sensor_data_file) > 0
