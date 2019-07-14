import json
from datetime import datetime
from threading import Lock


class SensorState(object):
    def __init__(self):
        self._lock = Lock()
        self._path = 'state.json'
        with open(self._path, 'r') as f:
            self._data = json.load(f)

    def set_last_activity(self):
        self._lock.acquire()
        try:
            self._data['lastActivity'] = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            self._write_state()
        finally:
            self._lock.release()

    def get_last_activity(self, ):
        self._lock.acquire()
        try:
            return self._data['lastActivity']
        finally:
            self._lock.release()

    def get_mode(self, ):
        self._lock.acquire()
        try:
            return self._data['mode']
        finally:
            self._lock.release()

    def set_mode(self, mode):
        self._lock.acquire()
        try:
            self._data['mode'] = mode
            self._write_state()
        finally:
            self._lock.release()

    def _write_state(self):
        with open(self._path, 'w+') as f:
            f.write(json.dumps(self._data))


sensor_state = SensorState()
