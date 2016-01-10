from tornado.websocket import WebSocketHandler
from tornado import gen
from tornado.escape import json_decode, json_encode, linkify
import tornado.web
from rdsclient import RedisClient
from uuid import uuid4

class MainHandler(tornado.web.RequestHandler): 
    def get(self, room=None):
        if not room:
            self.redirect('/room/1')

class RoomHandler(tornado.web.RequestHandler): 
    def get(self, room):
        print room
        self.render('index.html', room_list=xrange(1,5))



class WSHandler(WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(WSHandler, self).__init__(*args, **kwargs)
        rds  = RedisClient()
        self.client = rds.client
        self.pubsub = rds.pubsub

    @gen.engine
    def open(self, room=None):
        if not room:
            self.write_message({'status': 1, 'msg':'No such room'})
            self.close()
            return 
        
        self.room = str(room)
        self.new_msg_send = False
        self.pubsub.subscribe(**{self.room: self.on_messages_published})
        self.subscribed = True
        self.thread = self.pubsub.run_in_thread(sleep_time=0.001)
#        for i in self.pubsub.listen():
#            pass


    def on_messages_published(self, message):
        print message
        m = json_decode(message['data'])
        self.write_message(m)


    def on_message(self, data):
        try:
            datadecoded = json_decode(data)
            message = {
                    'uuid': str(uuid4()),
                    'body':linkify(datadecoded["body"]),
                    }
        except:
            self.write_message({'status': 1, 'msg': 'Bad input data'})
            return 

        try:

            print message
            msg_enc = json_encode(message)
            self.client.publish(self.room, msg_enc)
        except:
            self.write_message({'status':1, 'msg': 'Error writing data'})
            return 
#        self.write_message(message)
        return 


    def on_close(self):
        if hasattr(self, 'client'):
            if self.subscribed:
                self.pubsub.unsubscribe(self.room)
                self.subscribed = False
                self.thread.stop()

