from wsgiref.simple_server import make_server  
#from paste import httpserver  
from paste.deploy import loadapp  
import os  
 
def main():
    configfile = 'configure.ini' 
    appname = 'common'
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)
    #httpserver.serve(loadapp('config:configure.ini', relative_to = '.'), host = '127.0.0.1', port=8000)  
  
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()

if __name__ == '__main__':  
    main()
