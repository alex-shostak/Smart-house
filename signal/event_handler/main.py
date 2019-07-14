from paste import httpserver
from helpers.http import Api
from sensor import controller
from telegram import worker

# main WSGI endpoint
application = Api.as_wsgi

httpserver.serve(application, '192.168.88.15', 8081)