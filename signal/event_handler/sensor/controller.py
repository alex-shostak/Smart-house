from helpers.http import Api
import helpers.http_responses as http_responses
from sensor.state import sensor_state
from sensor.mode import SensorMode
from telegram.api import TelegramApi
from telegram.config import TelegramConfig


@Api.route('/get_mode')
def get_mode(request, response):
    log_activity = request.GET.get('log_activity') == 'true'
    if log_activity:
        sensor_state.set_last_activity()
    response.text = sensor_state.get_mode()


@Api.route('/save_event')
def save_event(request, response):
    sensor_state.set_mode(SensorMode.SLEEP)
    http_responses.ok(response)
    reply_markup = {"inline_keyboard": [[{ "text": "Я", "callback_data": "me" }],[{ "text": "Не я", "callback_data": "not_me" }]]}
    TelegramApi.send_message(token=TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID, text='Кто пришел домой?', reply_markup=reply_markup)




