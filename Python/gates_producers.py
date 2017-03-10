import random
import logging
from fwk.kafka.producer import KafkaProducer

# Logging
log_name = 'root'  
FORMAT = '%(asctime)s |%(name)s |%(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG) 

def passengers():
    '''Return passenger data
    '''
    return {'passengers': random.randint(1,9)}

def delay():
    '''Return random delay
    '''
    return random.randint(2, 30)

def inactivity():
    '''Return random inactivity delay
    '''
    return random.randint(1800, 7200)

gate_farm = KafkaProducer(topic_name='airport', serializer_kind='json')

[gate_farm.register(producer_name='A_{0}'.format(e), producer_kind='gate', 
                    data_func=passengers, delay_func=delay, inactivity_func=inactivity) for e in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']]
[gate_farm.register(producer_name='B_{0}'.format(e), producer_kind='gate', 
                    data_func=passengers, delay_func=delay, inactivity_func=inactivity) for e in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']]
[gate_farm.register(producer_name='C_{0}'.format(e), producer_kind='gate', 
                    data_func=passengers, delay_func=delay, inactivity_func=inactivity) for e in ['01', '02', '03', '04', '05', '06', '07', '08']]
[gate_farm.register(producer_name='D_{0}'.format(e), producer_kind='gate', 
                    data_func=passengers, delay_func=delay, inactivity_func=inactivity) for e in ['01', '02', '03', '04', '05']]

gate_farm.start()