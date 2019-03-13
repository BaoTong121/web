import webob
from webob.dec import wsgify
from webob import Request,Response


@wsgify
def application(request: Request):
    name = request.params.get('name')

    response = Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server  = make_server('0.0.0.0', 8000, application)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()