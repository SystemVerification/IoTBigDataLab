import random
import logging
from fwk.kafka.producer import KafkaProducer

# Logging
log_name = 'root'  
FORMAT = '%(asctime)s |%(name)s |%(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG) 

def words():
    '''Return words data
    '''
    s = '{0} {1} {2} {3} {4}'.format(random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9))
    return s

def delay():
    '''Return random delay
    '''
    return random.randint(1, 5)

def inactivity():
    '''Return random inactivity delay
    '''
    return random.randint(1, 5)

words_farm = KafkaProducer(topic_name='words', serializer_kind='string')

[words_farm.register(producer_name='words_generator_{0}'.format(e), producer_kind='word_generator',
                     data_func=words, delay_func=delay, inactivity_func=inactivity) 
                        for e in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']]
words_farm.start()