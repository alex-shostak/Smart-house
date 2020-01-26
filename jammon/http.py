import usocket as socket
import ussl as ssl


def get(host, uri, use_ssl=True):
    response = ''
    s = socket.socket()
    try:
        addr = socket.getaddrinfo(host, 443 if use_ssl else 80)[0][-1]
        s.connect(addr)

        req = bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (uri, host), 'utf8')
        if use_ssl:
            s = ssl.wrap_socket(s)
            s.write(req)
        else:
            s.send(req)
        while True:
            data = s.read(4096) if use_ssl else s.recv(4096)
            if data:
                response += str(data, 'utf8')
            else:
                break
        return _get_response_body(response)
    finally:
        s.close()


def _get_response_body(response):
    return response.split('\r\n\r\n')[1]
