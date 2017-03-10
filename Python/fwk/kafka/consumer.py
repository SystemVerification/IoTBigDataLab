import asyncio

from aiokafka import AIOKafkaConsumer
from fwk.kafka.cfg import Cfg

async def consumer_func(consumer):
    await consumer.start()
    async for msg in consumer:
        print(msg.value)

class KafkaConsumer:
    
    _cfg = Cfg.cfg()
    
    def __init__(self, topic_name):
        self._servers = self._cfg.kafka.servers
        self._topic_name = topic_name       
        self._tasks = []
        self._loop = asyncio.get_event_loop()
        
    def register(self):
        consumer = AIOKafkaConsumer(
            self._topic_name,
            loop=self._loop, 
            bootstrap_servers=self._servers)

        self._tasks.append(
            asyncio.ensure_future(
                consumer_func(consumer)))
        
    def start(self):
        self._loop.run_until_complete(asyncio.gather(*self._tasks))
        self._loop.close()
        