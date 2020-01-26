import utime


def heart_beat(display):
    display.brightness(0)

    display.fill(0)

    display.pixel(1, 0, 1)
    display.pixel(2, 0, 1)

    display.pixel(0, 1, 1)
    display.pixel(0, 2, 1)
    display.pixel(1, 3, 1)
    display.pixel(2, 4, 1)
    display.pixel(3, 5, 1)

    display.pixel(3, 1, 1)
    display.pixel(4, 0, 1)
    display.pixel(5, 0, 1)

    display.pixel(6, 1, 1)
    display.pixel(6, 2, 1)
    display.pixel(5, 3, 1)
    display.pixel(4, 4, 1)

    display.show()

    while True:
        display.brightness(0)
        utime.sleep(0.2)
        display.brightness(1)
        utime.sleep(0.2)
        display.brightness(2)
        utime.sleep(0.1)
        display.brightness(3)
        utime.sleep(0.1)
        display.brightness(4)
        utime.sleep(0.6)


def arrow_right(display):
    display.brightness(0)
    while True:
        display.fill(0)
        display.text('>', -1, 0, 1)
        display.show()

        utime.sleep(0.2)
        display.fill(0)
        display.text('>', 0, 0, 1)
        display.show()

        utime.sleep(0.2)
        display.fill(0)
        display.text('>', 1, 0, 1)
        display.show()

        utime.sleep(0.2)
        display.fill(0)
        display.text('>', 2, 0, 1)
        display.show()