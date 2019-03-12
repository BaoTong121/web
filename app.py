from urllib.parse import parse_qs
import webob
def application(environ:dict, start_response):
    request = webob.Request(environ)
    name  = request.params.get("name")
    print(request)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['hello {}'.format(name).encode()]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server  = make_server('0.0.0.0', 8000, application)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()