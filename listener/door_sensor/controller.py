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
        door_open_time = request.POST['data']
        print(door_open_time)
        DoorSensorModel.save_door_event(door_open_time)
        DoorSensorModel.set_sleep_mode()
        # call handler(send telegram message)



