import time
import json
from threading import Thread
from helpers.telegram import TelegramApi, TelegramState
from telegram_config import TelegramConfig


class TelegramWorker(object):
    def __init__(self):
        self._thread = Thread(target=self._handle_updates)
        self._state = TelegramState()
        #self._thread.daemon = True

    def start(self):
        self._thread.start()

    def _handle_updates(self):
        while self._thread.is_alive:

            last_update_id = self._state.get_last_update()
            updates = json.loads(TelegramApi.get_updates(TelegramConfig.BOT_TOKEN, last_update_id + 1))

            for upd in updates['result']:
                update_id = upd['update_id']
                self._state.set_last_update(update_id)

                message_text = upd['callback_query']['message']['text']
                if message_text == 'Кто пришел домой?':
                    reply_data = upd['callback_query']['data']
                    sender_name = upd['callback_query']['from']['first_name']
                    message_id = upd['callback_query']['message']['message_id']
                    self._state.set_last_message(message_id)
                    if reply_data == 'me':
                        TelegramApi.send_message(TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID, text=f'{sender_name} дома, сигнализация отключена')
                    else:
                        self._state.set_negative_response(sender_name)
                        negative_resp_cnt = self._state.get_negative_resp_cnt()
                        recipient_count = TelegramApi.get_chat_members_cnt(TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID)
                        if negative_resp_cnt >= recipient_count:
                            TelegramApi.send_message(TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID,
                                                     text=f'ТРЕВОГА ТРЕВОГА!!! Волк украл зайчат')


            time.sleep(5)



worker = TelegramWorker()
worker.start()