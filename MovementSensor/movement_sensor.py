import os
import machine
import time_

sensor_pin = machine.Pin(4, machine.Pin.IN)
folder = 'sensor_data'
try:
    os.mkdir(folder)
except:
    pass
path = folder + '/movement.txt'


def movement_detected():
    return sensor_pin.value() == 0


def save_data():
    with open(path, 'a') as f:
        print(time_.get_time(), file=f)


def get_data():
    with open(path, 'r') as f:
        return f.readlines()
