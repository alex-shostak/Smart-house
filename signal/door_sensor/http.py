import config
import socket


def get(uri):
    response = ''
    addr = socket.getaddrinfo(config.Server.address, config.Server.port)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (uri, config.Server.address), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            response += str(data, 'utf8')
        else:
            break
    s.close()
    return _get_response_body(response)


def _get_response_body(response):
    return response.split('\r\n\r\n')[1]
