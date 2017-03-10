[Back ...](../README.md)

# Python area

Example logic as Python code.

This requires *Python 3.6*

Required Python packages (to install with pip):
* aiokafka - async IO Kafka streaming
* bunch - konvert Python dict to an object
* PyYAML - YAML support used for configuration files

Possible IDE: Eclipse + PyDev
* Import this area as a PyDev project in Eclipse


## Framework

Directory: __fwk__

Framework area

Directory: __fwk/kafka__

Kafka streaming framework with some encapsulation for easy creation of multiple streams.
Build-in configuration mechanism for system parameters.

## Examples

Streams generators

Generating random numbers: __words_producers.py__

Generating random airport gate passenger trafic: __gates_producers.py__