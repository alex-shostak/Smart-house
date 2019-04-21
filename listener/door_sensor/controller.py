from helpers.http import Api
import helpers.http_responses as http_responses
from door_sensor.model import DoorSensorModel


class DoorSensorController(object):
    @staticmethod
    @Api.route('/get_mode')
    def get_mode(request, response):
        # authenticate?
        log_activity = request.GET.get('log_activity') == 'true'
        if log_activity:
            DoorSensorModel.set_last_activity()
        response.text = DoorSensorModel.get_mode()

    @staticmethod
    @Api.route('/set_mode')
    def set_mode(request, response):
        # authenticate?
        mode = request.GET.get('mode')
        if mode is None:
            http_responses.bad_request(response)
        DoorSensorModel.set_mode(mode)
        http_responses.ok(response)

    @staticmethod
    @Api.route('/post_data')
    def post_data(request, response):
        event_name = request.GET.get('data')
        print(event_name)
        DoorSensorModel.save_door_event(event_name)
        DoorSensorModel.set_sleep_mode()
        http_responses.ok(response)
        # call handler(send telegram message)



