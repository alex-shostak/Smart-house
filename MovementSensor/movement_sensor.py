import os
import machine
import time_
import config

sensor_pin = machine.Pin(config.GPIO.sensor_pin, machine.Pin.IN)
folder = 'sensor_data'
try:
    os.mkdir(folder)
except:
    pass
path = folder + '/movement.txt'


def movement_detected():
    return sensor_pin.value() == 1


def save_data():
    with open(path, 'a') as f:
        print(time_.get_time(), file=f)


def get_data():
    with open(path, 'r') as f:
        return f.readlines()
