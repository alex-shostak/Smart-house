import socket as socket
import ssl as ssl
import gc


def get(host, uri, use_ssl=True):
    resp = ''
    s = socket.socket()
    try:
        s.settimeout(30)
        addr = socket.getaddrinfo(host, 443 if use_ssl else 80)[0][-1]
        gc.collect()
        s.connect(addr)

        req = bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (uri, host), 'utf8')
        if use_ssl:
            s = ssl.wrap_socket(s)
            s.write(req)
        else:
            s.send(req)
        while True:
            data = s.read(128) if use_ssl else s.recv(128)
            if data:
                resp += str(data, 'utf8')
            else:
                break
        return _get_response_body(resp)
    finally:
        s.close()


def _get_response_body(resp):
    return resp.split('\r\n\r\n')[1]
