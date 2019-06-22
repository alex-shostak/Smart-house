def not_found(response):
    response.status_code = 404
    response.text = u'resource not found'


def internal_error(response):
    response.status_code = 500
    response.text = u'internal server error'


def bad_request(response):
    response.status_code = 400
    response.text = u'bad request'


def forbidden(response):
    response.status_code = 403
    response.text = u'forbidden'


def ok(response):
    response.status_code = 200
    response.text = u'OK'


def unauthorized(response):
    response.status_code = 401
    response.text = u'unauthorized'


def service_unavailable(response):
    response.status_code = 503
    response.text = u'service unavailable'