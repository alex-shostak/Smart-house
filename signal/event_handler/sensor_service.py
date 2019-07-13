import os
import json
import uuid
from datetime import datetime
from threading import Lock


STATE_PATH = os.path.join('door_sensor', 'sensor_state.json')
EVENTS_PATH = os.path.join('door_sensor', 'events')
STATE_LOCK = Lock()


def set_last_activity():
    STATE_LOCK.acquire()
    try:
        state = get_state()
        with open(STATE_PATH, 'w+') as f:
            state['lastActivity'] = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            f.write(json.dumps(state))
    finally:
        STATE_LOCK.release()


def get_last_activity():
    STATE_LOCK.acquire()
    try:
        state = get_state()
        return state['lastActivity']
    finally:
        STATE_LOCK.release()


def get_mode():
    STATE_LOCK.acquire()
    try:
        state = get_state()
        return state['mode']
    finally:
        STATE_LOCK.release()


def set_mode(mode):
    STATE_LOCK.acquire()
    try:
        state = get_state()
        with open(STATE_PATH, 'w+') as f:
            state['mode'] = mode
            f.write(json.dumps(state))
    finally:
        STATE_LOCK.release()


def set_sleep_mode():
    set_mode("S")


def save_event(event_name):
    filename = os.path.join(EVENTS_PATH, uuid.uuid4().hex)
    with open(filename, 'w+') as f:
        f.write(event_name)


#todo: кешировать в память
def get_state():
    with open(STATE_PATH, 'r') as f:
        return json.load(f)