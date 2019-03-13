import webob
from webob.dec import wsgify
from webob import Request,Response
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
        return Response(status=404,body='not found')

    @wsgify
    def __call__(self,request:Request)->Response:
        return self.ROUTE.get(request.path,self.default_handler)(request)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    application.register('/hello',hello)
    application.register('/', index)

    server  = make_server('0.0.0.0', 8000, application())

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()