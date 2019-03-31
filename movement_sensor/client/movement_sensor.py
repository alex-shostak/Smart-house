import os
import machine
import utime
import time_
import config

sensor_pin = machine.Pin(config.GPIO.sensor_pin, machine.Pin.IN)
folder = 'sensor_data'
try:
    os.mkdir(folder)
except:
    pass

path = folder + '/movement.txt'
_mode = "SLEEP"
_last_mode_check_time = utime.localtime()


def is_time_to_check_mode():
    return utime.localtime() > time_.add_seconds(_last_mode_check_time, 20)


def set_mode(mode):
    global _last_mode_check_time, _mode
    _last_mode_check_time = utime.localtime()
    _mode = mode


def is_sleep_mode():
    return _mode == "SLEEP"


def movement_detected():
    return sensor_pin.value() == 1


def save_data():
    with open(path, 'w') as f:
        print(time_.get_time(), file=f)


def delete_data():
    with open(path, 'w'):
        pass


def data_exists():
    return os.path.isfile(path) and os.path.getsize(path) > 0


def get_data():
    with open(path, 'r') as f:
        return f.readlines()
