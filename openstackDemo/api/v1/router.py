import wsgi

class ControllerTest(object):
    def __init__(self):
        print "ControllerTest!!!!"
    def test(self,req):
          print "req",req
          return {
            'name': "test",
            'properties': "test"
        }
    def root(self,req):
        return {
                'version':"0.0.4"
        }


class MyRouterApp(wsgi.Router):
      '''
      app
      '''
      def __init__(self,mapper):
          controller = ControllerTest()
          mapper.connect('/test',
                       controller=wsgi.Resource(controller),
                       action='test',
                       conditions={'method': ['GET']})
          mapper.connect('/',
                       controller=wsgi.Resource(controller),
                       action='root',
                       conditions={'method': ['GET']})
          super(MyRouterApp, self).__init__(mapper)
