from fwk.kafka.consumer import KafkaConsumer

events_logger = KafkaConsumer('airport')
events_logger.register()
events_logger.start()