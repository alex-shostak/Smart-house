import requests
import json


class TelegramApi:
    @staticmethod
    def send_message(token, chat_id, text, reply_markup):
        response = requests.get(
            f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}?&reply_markup={json.dumps(reply_markup)}')
        return response.status_code, response.text

