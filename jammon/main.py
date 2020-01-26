import utime
import log
import wifi
import time_
import max7219
from machine import Pin, SPI
import jam_monitor

display = None


def init():
    log.remove()

    spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
    global display
    display = max7219.Matrix8x8(spi, Pin(15), 1)

    display.brightness(1)
    display.fill(0)
    display.text('s', 0, 0, 1)
    display.show()
    utime.sleep(1)
    try:
        wifi.disable_ap()
        wifi.connect()

        display.fill(0)
        display.text('w', 0, 0, 1)
        display.show()
        utime.sleep(1)

        time_.set_time()
        display.fill(0)
        display.text('t', 0, 0, 1)
        display.show()
        utime.sleep(1)

        jam_monitor.read_conf()
        display.fill(0)
        display.text('j', 0, 0, 1)
        display.show()
        utime.sleep(1)
    except Exception as e:
        display.brightness(0)
        display.fill(0)
        display.text('E', 0, 0, 1)
        display.show()
        raise e
        #log.write("init: " + str(e))


def loop():
    #log.append('starting main loop')
    display.fill(0)
    display.text('l', 0, 0, 1)
    display.show()
    utime.sleep(1)
    while True:
        try:
            utime.sleep(1)
            jam_monitor.check_jams(display)
        except Exception as e:
            display.brightness(0)
            display.fill(0)
            display.text('E', 0, 0, 1)
            display.show()
            #log.write("loop: " + str(e))


init()
loop()
