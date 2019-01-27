import utime
import machine

diode_pin = machine.Pin(2, machine.Pin.OUT)


def on():
    diode_pin.off()


def off():
    diode_pin.on()


def blink(times=2, delay=0.4):
    for i in range(times):
        on()
        utime.sleep(delay)
        off()
        utime.sleep(delay)
