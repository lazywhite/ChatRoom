from redis import ConnectionPool, StrictRedis
from config import redis_host, redis_port

pool = ConnectionPool(host=redis_host, port=redis_port)
class RedisClient(object):
    def __init__(self, host=None, port=None):
        self._client = StrictRedis(connection_pool=pool)

    @property
    def client(self):
        return self._client

    @property
    def pubsub(self):
        return self._client.pubsub()
