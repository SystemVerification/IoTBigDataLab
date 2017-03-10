import asyncio
import random
import json
#import datetime
from aiokafka import AIOKafkaProducer
from fwk.kafka.cfg import Cfg
from bunch import bunchify

async def producer_func(producer, **kwargs):
    '''Produce Kafka events in a loop.
            Wait some delay to send the event
            Wait some additional delay after a number of events 
          
       Parameters:
           producer - AIOKafkaProducer - async io producer object
           producer_name - producer name
           producer_kind - producer kind/group name
           topic_name - Kafka event topic name
           data_func - generator that produces the topic data
           delay_func - function generating a delay interval to sleep between topic data items in a series of data items
           inactivity_func - function generating an inactivity interval between series of topic data items
           serializer_kind - how to serialize/encode data. Possible encodings 'string', 'json'         
    '''
    _pp = bunchify(kwargs)
    await producer.start()
    cycles = random.randint(10, 50)
    while True:
        cycles = cycles - 1
        await asyncio.sleep(_pp.delay_func())
        if _pp.serializer_kind == 'string':
            data = _pp.data_func()
        else:
            data = {
                #'time_utc': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                'name': _pp.producer_name,
                'kind': _pp.producer_kind,
                'value': _pp.data_func()
                }
        await producer.send(_pp.topic_name, data)
        if cycles == 0:
            await asyncio.sleep(_pp.inactivity_func())
            cycles = random.randint(10, 50)

class KafkaProducer:
    
    _cfg = Cfg.cfg()
    
    def __init__(self, **kwargs):
        '''Initialize the Kafka producer object
           Parameters:
            topic_name - Kafka event topic name
            serializer_kind - how to serialize/encode data. Possible encodings 'string', 'json'           
        '''
        _pp = bunchify(kwargs)
        self._servers = self._cfg.kafka.servers
        self._topic_name = _pp.topic_name
        self._serializer_kind = _pp.serializer_kind     
        self._tasks = []
        self._loop = asyncio.get_event_loop()
        if self._serializer_kind == 'string':
            self._value_serializer = self._serializer
        else:
            self._value_serializer = self._json_serializer
        
    def register(self, **kwargs):
        '''Register with Kafka in order to produce events
        
           Parameters:
               producer_name - producer name
               producer_kind - producer kind name
               data_func - generator that produces the topic data
               delay_func - function generating a delay interval to sleep between topic data items in a series of data items
               inactivity_func - function generating an inactivity interval between series of topic data items
        '''
        producer = AIOKafkkwearaProducer(
            loop=self._loop, 
            bootstrap_servers=self._servers,
            value_serializer=self._serializer)

        self._tasks.append(
            asyncio.ensure_future(producer_func(producer, serializer_kind=self._serializer_kind, topic_name=self._topic_name, **kwargs)))
        
    def start(self):
        self._loop.run_until_complete(asyncio.gather(*self._tasks))
        self._loop.close()
        
    def _json_serializer(self, value):
        return json.dumps(value).encode()
    
    def _serializer(self, value):
        return value.encode()