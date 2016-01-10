import tornado.ioloop
import tornado.web
from config import port

class MainHandler(tornado.web.RequestHandler): 
    def get(self):
        self.render('index.html')
        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port) 
    tornado.ioloop.IOLoop.current().start()
