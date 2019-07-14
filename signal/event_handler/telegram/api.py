import requests
import json
import urllib


class TelegramApi:
    @staticmethod
    def send_message(token, chat_id, text, reply_markup=None):
        if reply_markup:
            reply_markup_str = f'&reply_markup={json.dumps(reply_markup)}'
        else:
            reply_markup_str = ''
        encoded_text = urllib.parse.urlencode({'text': text})
        response = requests.get(
            f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&{encoded_text}'+reply_markup_str)
        return response.status_code, response.text

    @staticmethod
    def get_updates(token, offset):
        response = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset={offset}')
        return response.text

    @staticmethod
    def get_chat_members_cnt(token, chat_id):
        response = requests.get(f'https://api.telegram.org/bot{token}/getChatMembersCount?chat_id={chat_id}')
        return json.loads(response.text)['result'] - 1
