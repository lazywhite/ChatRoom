import tornado.ioloop
import tornado.web
from handlers import MainHandler, RoomHandler, WSHandler

from config import port, template_path, static_path

        
def make_app():
    return tornado.web.Application(
       handlers=[
            tornado.web.URLSpec(r"/", MainHandler, name="index"),
            tornado.web.URLSpec(r"/room/(.*)", RoomHandler, name="room"),
            tornado.web.URLSpec(r"/ws/(.*)", WSHandler, name="chat"),
        ]
    ,
    template_path=template_path, 
    static_path=static_path,
    debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(port) 
    print "listening on: http://localhost:%d" % port
    tornado.ioloop.IOLoop.current().start()
