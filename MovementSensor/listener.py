import socket
import led
import log


class Listener(object):
    def __init__(self):
        self._socket = None

    def start(self, port):
        try:
            self._socket = socket.socket()
            self._socket.bind(("", port))
            self. _socket.listen(1)
            log.write('listener started on port ' + str(port))
        except Exception as e:
            log.write("Listener.start: " + str(e))
            led.on()
            raise

    def listen(self):
        try:
            client, address = self._socket.accept()
            cl_file = client.makefile('rwb', 0)
            request = b''
            while True:
                line = cl_file.readline()
                if not line or line == b'\r\n':
                    break
                request += line
            self.on_request(request, client)
            client.close()
        except Exception as e:
            log.write("Listener.listen: " + str(e))
            led.blink(1, 1)

    def on_request(self, request, client):
        pass


listener = Listener()

