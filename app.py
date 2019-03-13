import webob
from webob.dec import wsgify
from webob import Request,Response
from webob import exc


def hello(request):
    name = request.params.get('name')
    response = Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response
def index(request):
    return Response(body='hello world',status=200,content_type='text/plain')


class application():
    ROUTE = {}

    @classmethod
    def register(cls, path, handler):
        cls.ROUTE[path] = handler
    def default_handler(self,request):
        raise exc.HTTPNotFound('Not fount')

    @wsgify
    def __call__(self,request:Request)->Response:
        try:
            return self.ROUTE[request.path](request)
        except KeyError:
            raise exc.HTTPNotFound('Not Fount')


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    application.register('/hello',hello)
    application.register('/', index)

    server  = make_server('0.0.0.0', 8000, application())

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()