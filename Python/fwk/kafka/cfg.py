import yaml
import logging
from bunch import bunchify
from os import path
from fwk.util.singleton import Singleton
from fwk.util.helper import dict_merge

_log = logging.getLogger(__name__)

class Cfg(object):
    '''Configuration class for the application.
    '''

    __metaclass__ = Singleton
    
    _cfg = None

    @classmethod
    def cfg(cls):
        if cls._cfg is not None:
            return cls._cfg
        
        _local_cfg = None
        _local_cfg_file = path.join(path.dirname(path.dirname(path.dirname(__file__))), 'local.yaml')
        if path.exists(_local_cfg_file):
            with open(_local_cfg_file, 'r') as _file:
                _log.debug("Reading configuration from: '{0}'".format(_local_cfg_file))
                _local_cfg = yaml.load(_file)

        _cfg = None
        _cfg_file = path.join(path.dirname(__file__), 'cfg.yaml')
        if path.exists(_cfg_file):
            with open(_cfg_file, 'r') as _file:
                _log.debug("Reading configuration from: '{0}'".format(_cfg_file))
                _cfg = yaml.load(_file)

        if _local_cfg is not None:
            cls._cfg =  bunchify(dict_merge(_cfg, _local_cfg))
        else:
            cls._cfg = bunchify(_cfg)
        
        return cls._cfg

if __name__ == '__main__':
    # Logging
    log_name = 'root'
    FORMAT = '%(asctime)s |%(name)s |%(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    _log.debug(Cfg.cfg().driver.kind)
    _log.debug(Cfg.cfg().driver.path)
