from helpers.http import Api
from paste import httpserver
from door_sensor.controller import DoorSensorController

# main WSGI endpoint
application = Api.as_wsgi

httpserver.serve(application, '192.168.88.15', 8081)