import redis
from config import redis_host, redis_port

class RedisClient(object):
    def __init__(self, host=None, port=None):
        if host is None:
            host = redis_host

        if port is None:
            port = redis_port

        self._client = redis.StrictRedis(host='localhost', port=6379, db=0)

    @property
    def client(self):
        return self._client
