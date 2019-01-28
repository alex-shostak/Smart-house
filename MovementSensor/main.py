import utime
import log
import led
import wifi
import config
import movement_sensor
from listener import listener
import time_


class Main(object):
    def __init__(self):
        log.remove()
        wifi.connect()
        led.blink(1)
        wifi.disable_ap()
        led.blink(1)
        time_.set_time()
        led.blink(1)
        listener.start(port=config.Listener.port)
        listener.on_request = self.on_request
        led.blink(1)

    def loop(self):
        log.write('starting main loop')
        while True:
            try:
                if movement_sensor.movement_detected():
                    movement_sensor.save_data()
                #listener.listen()
                utime.sleep(1)
            except Exception as e:
                log.write("Main.loop: " + str(e))
                led.blink(1, 1)

    def on_request(self, request, client):
        for line in movement_sensor.get_data():
            client.send(line.replace('\n', '\r\n').encode())


Main().loop()
