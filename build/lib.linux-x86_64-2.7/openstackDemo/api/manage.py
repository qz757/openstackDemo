class ShowVersion(object):
      '''
      app
      '''
      def __init__(self,version):
          self.version = version
      def __call__(self,environ,start_response):
            start_response("200 OK",[("Content-type", "text/plain")])
            return ["Paste Deploy wsgi server: Version = 0.0.4",]
      @classmethod
      def factory(cls,global_conf,**kwargs):
          print 'factory'
          print "kwargs:",kwargs
          return ShowVersion(kwargs['version'])

class LogFilter(object):
      '''
      Log
      '''
      def __init__(self,app):
          self.app = app
      def __call__(self,environ,start_response):
          print 'you can write log.'
          return self.app(environ,start_response)
      @classmethod
      def factory(cls,global_conf,**kwargs):
          return LogFilter
