import time
import json
from threading import Thread
from helpers.telegram import TelegramApi


class TelegramWorker(object):
    def __init__(self):
        self._thread = Thread(target=self._handle_updates)
        #self._thread.daemon = True

    def start(self):
        self._thread.start()

    def _handle_updates(self):
        while self._thread.is_alive:
            #todo: pass last update id
            updates = json.loads(TelegramApi.get_updates('752125381:AAHZtMmxpRbQKF8aTOE1aTyP1zAyX9XD-SY', 954161960))
            if not updates['ok']:
                print(updates)
                continue
            for upd in updates['result']:
                message_text = upd['callback_query']['message']['text']
                if message_text == 'Кто пришел домой?':
                    reply_data = upd['callback_query']['data']
                    update_id = upd['update_id']
                    #todo: store last update
                    if reply_data == 'me':
                        sender_name = upd['callback_query']['from']['first_name']
                        TelegramApi.send_message('752125381:AAHZtMmxpRbQKF8aTOE1aTyP1zAyX9XD-SY', chat_id='-1001375176524', text=f'{sender_name} дома, сигнализация будет отключена')
                        #todo: turn off sensor
                    else:
                        pass
                        """-get recipients count from config/chat
                           -store count of negative responses linked to update id(increment)
                           -if negative resp count >= recipients count then send alert message"""
            time.sleep(5)



worker = TelegramWorker()
worker.start()