from helpers.http import Api
import helpers.http_responses as http_responses
import door_sensor.model as model


@Api.route('/get_mode')
def get_mode(request, response):
    # authenticate?
    log_activity = request.GET.get('log_activity') == 'true'
    if log_activity:
        model.set_last_activity()
    response.text = model.get_mode()


@Api.route('/set_mode')
def set_mode(request, response):
    # authenticate?
    mode = request.GET.get('mode')
    if mode is None:
        http_responses.bad_request(response)
        model.set_mode(mode)
    http_responses.ok(response)


@Api.route('/save_event')
def save_event(request, response):
    event_name = request.GET.get('name')
    model.save_event(event_name)
    model.set_sleep_mode()
    http_responses.ok(response)
    # call handler(send telegram message)




