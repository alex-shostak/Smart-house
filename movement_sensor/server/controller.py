from helpers.http import Api
from model import MovementSensorModel


class MovementSensorController(object):
    def __init__(self, model):
        self._model = model  # type: MovementSensorModel

    @Api.route('/get_mode')
    def get_mode(self, request, response):
        pass
        # authenticate?
        self._model.set_last_activity()
        response.text = self._model.get_mode()

    @Api.route('/set_mode')
    def set_mode(self, request, response):
        pass
        # authenticate?
        mode = request.POST['mode']
        self._model.set_mode(mode)

    @Api.route('/post_data')
    def post_data(self, request, response):
        movement_time = request.POST['data']
        self._model.save_movement_time(movement_time)
        self._model.set_sleep_mode()
        # call handler(send telegram message)
