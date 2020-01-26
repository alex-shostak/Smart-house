import utime
import log
import wifi
import time_
from max7219 import Matrix8x8
from machine import Pin, SPI
import jam_monitor

display = None


def init():
    log.remove()

    spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
    global display
    display = Matrix8x8(spi, Pin(15), 1)
    display.brightness(1)
    show_text('s')
    try:
        wifi.disable_ap()
        wifi.connect()
        show_text('w')

        time_.set_time()
        show_text('t')

        jam_monitor.read_conf()
        show_text('j')
    except Exception as e:
        display.brightness(0)
        show_text('E')
        log.write("init: " + str(e))
        raise e


def loop():
    log.append('starting main loop')
    show_text('m')
    while True:
        try:
            utime.sleep(1)
            jam_monitor.check_jams(display)
        except Exception as e:
            show_text('E')
            log.write("loop: " + str(e))


def show_text(text):
    display.fill(0)
    display.text(text, 0, 0, 1)
    display.show()
    utime.sleep(1)


init()
loop()
