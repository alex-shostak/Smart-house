from webob import Request, Response


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
        route = Api.routes.get(request.path_info.upper())
        if route is not None:
            route(request, response)
        else:
            # todo: send 404
            pass
        
    @staticmethod
    def route(path):
        def decorator(method):
            Api.add_route(path, method)

        return decorator
