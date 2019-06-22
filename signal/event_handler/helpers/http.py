from traceback import format_exc
from webob import Request, Response
import helpers.http_responses as http_responses


class Api:
    routes = {}

    @staticmethod
    def as_wsgi(environ, start_response):
        """
        main WSGI endpoint(for details: support https://ru.wikipedia.org/wiki/WSGI)
        """
        # passing environ object into webob.Request
        request = Request(environ)
        # creating empty Response object
        response = Response()
        Api.exec_route(request, response)
        return response(environ, start_response)

    @staticmethod
    def add_route(path, method):
        Api.routes[path.upper()] = method

    @staticmethod
    def exec_route(request, response):
        try:
            route_ = Api.routes.get(request.path_info.upper())
            if route_ is not None:
                route_(request, response)
            else:
                http_responses.not_found(response)
                pass
        except:
            print(format_exc())
            http_responses.internal_error(response)
        
    @staticmethod
    def route(path):
        def decorator(method):
            Api.add_route(path, method)

        return decorator