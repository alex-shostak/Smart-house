import json


class TelegramState(object):
    def __init__(self):
        self._path = 'state.json'
        with open(self._path, 'r') as f:
            self._data = json.load(f)

    def get_last_update(self):
        return self._data['last_update']

    def set_last_update(self, update_id):
        if update_id > self._data['last_update']:
            self._data['last_update'] = update_id
            self._write_state()

    def set_last_message(self, message_id):
        if message_id > self._data['last_message']:
            self._data['last_message'] = message_id
            self._data['negative_responses'] = []
            self._write_state()

    def get_negative_resp_cnt(self):
        return len(self._data['negative_responses'])

    def set_negative_response(self, sender):
        if sender not in self._data['negative_responses']:
            self._data['negative_responses'].append(sender)
            self._write_state()

    def _write_state(self):
        with open(self._path, 'w+') as f:
            f.write(json.dumps(self._data))