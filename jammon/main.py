import utime
import log
import wifi
import time_
import max7219
from machine import Pin, SPI

display = None


def init():
    log.remove()

    spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
    global display
    display = max7219.Matrix8x8(spi, Pin(15), 1)
    # global display

    display.brightness(1)
    display.fill(0)
    display.text('s', 0, 0, 1)
    display.show()
    utime.sleep(1)

    wifi.connect()
    wifi.disable_ap()

    display.fill(0)
    display.text('w', 0, 0, 1)
    display.show()
    utime.sleep(1)

    # time_.set_time()


def loop():
    try:
        log.append('starting main loop')
        display.fill(0)
        display.text('l', 0, 0, 1)
        display.show()
        utime.sleep(1)

        while True:
            utime.sleep(1)
    except Exception as e:
        display.brightness(0)
        display.fill(0)
        display.text('E', 0, 0, 1)
        display.show()
        log.write("loop: " + str(e))


init()
loop()
