class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else: # run __init__ every time the class is called
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]