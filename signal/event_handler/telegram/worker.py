import time
import json
from threading import Thread
from traceback import format_exc
from telegram.api import TelegramApi
from telegram.state import TelegramState
from telegram.config import TelegramConfig
from sensor.state import sensor_state
from sensor.mode import SensorMode


class TelegramWorker(object):
    def __init__(self):
        self._thread = Thread(target=self._handle_updates)
        self._state = TelegramState()
        self._thread.daemon = True
        if sensor_state.get_mode() == SensorMode.SLEEP:
            sensor_state.set_mode(SensorMode.SLEEP)
            self._send_turn_on_question()

    def start(self):
        self._thread.start()

    def _handle_updates(self):
        while self._thread.is_alive:
            try:
                last_update_id = self._state.get_last_update()
                updates = json.loads(TelegramApi.get_updates(TelegramConfig.BOT_TOKEN, last_update_id + 1))
                # todo: ignore other chats
                for upd in updates['result']:
                    update_id = upd['update_id']

                    if upd['callback_query']['message']['text'] == 'Кто пришел домой?':
                        self._handle_arrival_response(upd)
                    elif upd['callback_query']['data'] == 'turn_on':
                        self._handle_turn_on_response()

                    self._state.set_last_update(update_id)
                time.sleep(1)
            except:
                print(format_exc())
                # todo: write log

    def _handle_arrival_response(self, upd):
        reply_data = upd['callback_query']['data']
        sender_name = upd['callback_query']['from']['first_name']
        message_id = upd['callback_query']['message']['message_id']
        self._state.set_last_message(message_id)
        if reply_data == 'me':
            self._send_arrived_message(sender_name)
            self._send_turn_on_question()
        else:
            self._state.set_negative_response(sender_name)
            negative_resp_cnt = self._state.get_negative_resp_cnt()
            recipient_count = self._get_recipient_count()
            if negative_resp_cnt >= recipient_count:
                self._send_alert_message()
                self._send_turn_on_question()

    @staticmethod
    def _handle_turn_on_response():
        sensor_state.set_mode(SensorMode.ACTIVE)
        TelegramApi.send_message(TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID,  text=f'Сигнализация включена')

    @staticmethod
    def _send_arrived_message(sender_name):
        message_text = f'{sender_name} дома, сигнализация отключена'
        TelegramApi.send_message(TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID, text=message_text)

    @staticmethod
    def _send_turn_on_question():
        reply_markup = {"inline_keyboard": [[{"text": "Включить сигнализацию", "callback_data": "turn_on"}]]}
        alert_emoji = '\U0001F6A8'
        TelegramApi.send_message(token=TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID,
                                 text=alert_emoji, reply_markup=reply_markup)

    @staticmethod
    def _get_recipient_count():
        return TelegramApi.get_chat_members_cnt(TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID)

    @staticmethod
    def _send_alert_message():
        message_text = 'ТРЕВОГА ТРЕВОГА!!! Волк украл зайчат'
        TelegramApi.send_message(TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID, text=message_text)


worker = TelegramWorker()
worker.start()
