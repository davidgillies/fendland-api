from tornado import websocket, web, ioloop
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fenland_api.settings")
from tornado.options import options, define, parse_command_line
#from django.core.wsgi import get_wsgi_application
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import datetime
import json
import signal
import time
from tornado.options import options, define
 
define('port', type=int, default=8080)

def shutdown(server):
    ioloop = tornado.ioloop.IOLoop.instance()
    server.stop()
    
    def finalize():
        ioloop.stop()
        
    ioloop.add_timeout(time.time() + 1.5, finalize)

cl = []

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)

class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.finish()
        status = self.get_argument("status")
        value = self.get_argument("value")
        data = {"value" : value, "status": status}
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)
            

    @web.asynchronous
    def post(self):
        pass

 
class NoCacheStaticHandler(tornado.web.StaticFileHandler):
  """ Request static file handlers for development and debug only.
  It disables any caching for static file.
  """
  def set_extra_headers(self, path):
    self.set_header('Cache-Control', 'no-cache, must-revalidate')
    self.set_header('Expires', '0')
    now = datetime.datetime.now()
    expiration = datetime.datetime(now.year-1, now.month, now.day)
    self.set_header('Last-Modified', expiration)
 
 
def main():
  #### my fix
  #application = get_wsgi_application()
  #wsgi_app = tornado.wsgi.WSGIContainer(
  #    application)
  ####
  tornado_app = tornado.web.Application(
    [
     # (r'/static/(.*)', web.StaticFileHandler, {'path': 'U:/Data/fenland_api/fendland-api/static'}),
      (r'/ws', SocketHandler),
      (r'/t_api', ApiHandler),
    #  ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
      ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  server.listen(options.port)
  signal.signal(signal.SIGINT, lambda sig, frame: shutdown(server))
  tornado.ioloop.IOLoop.instance().start()
 
if __name__ == '__main__':
  main()