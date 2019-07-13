from helpers.http import Api
import helpers.http_responses as http_responses
import sensor_service as service
from helpers.telegram import TelegramApi
from telegram_config import TelegramConfig


@Api.route('/get_mode')
def get_mode(request, response):
    log_activity = request.GET.get('log_activity') == 'true'
    if log_activity:
        service.set_last_activity()
    response.text = service.get_mode()


@Api.route('/save_event')
def save_event(request, response):
    event_name = request.GET.get('name')
    service.save_event(event_name)
    service.set_sleep_mode()
    http_responses.ok(response)
    reply_markup = {"inline_keyboard": [[{ "text": "Я", "callback_data": "me" }],[{ "text": "Не я", "callback_data": "not_me" }]]}
    TelegramApi.send_message(token=TelegramConfig.BOT_TOKEN, chat_id=TelegramConfig.CHAT_ID, text='Кто пришел домой?', reply_markup=reply_markup)




