import webob
from webob.dec import wsgify
from webob import Request,Response
from webob import exc
import re



class application():
    ROUTE = []
    @classmethod
    def register(cls, pattern):
        def wrap(handler):
            cls.ROUTE.append((re.compile(pattern),handler))
            return handler
        return wrap
    @wsgify
    def __call__(self,request:Request)->Response:
        for pattern, handler in self.ROUTE:
            if pattern.match(request.path):
                return handler(request)
        raise exc.HTTPNotFound('Not Fount')



@application.register('^/hello$')
def hello(request):
    name = request.params.get('name','anonymous')
    response = Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response
@application.register('^/$')
def index(request):
    return Response(body='hello world',status=200,content_type='text/plain')





if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server  = make_server('0.0.0.0', 8000, application())

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()