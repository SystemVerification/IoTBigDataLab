"""
.. module:: framework_util_helper
   :platform: Unix, Windows
   :synopsis: Application Page Object

.. moduleauthor:: Piotr Nestorow <piotrn@axis.com>

Different helper functions.
"""
import time
import datetime

def enum(**enums):
    '''Create an enumeration type
    
    :return: enumeration type
    '''
    enums['items'] = enums.values()
    return type('Enum', (), enums)

def epoch():
    ''' Return epoch in seconds as a string
    '''
    return '{0:.0f}'.format(time.mktime(datetime.datetime.now().timetuple()))

def dict_merge(a, b):
    """Merges b into a and return merged result

    NOTE: tuples and arbitrary objects are not handled as it is totally ambiguous what should happen"""
    key = None
    # ## debug output
    # sys.stderr.write("DEBUG: %s to %s\n" %(b,a))
    try:
        if a is None or isinstance(a, str)  or isinstance(a, int) or isinstance(a, float):
            # border case for first run or if a is a primitive
            a = b
        elif isinstance(a, list):
            # lists can be only appended
            if isinstance(b, list):
                # merge lists
                a.extend(b)
            else:
                # append to list
                a.append(b)
        elif isinstance(a, dict):
            # dicts must be merged
            if isinstance(b, dict):
                for key in b:
                    if key in a:
                        a[key] = dict_merge(a[key], b[key])
                    else:
                        a[key] = b[key]
            else:
                raise Exception('Cannot merge non-dict "%s" into dict "%s"' % (b, a))
        else:
            raise Exception('NOT IMPLEMENTED "%s" into "%s"' % (b, a))
    except TypeError as e:
        raise Exception('TypeError "%s" in key "%s" when merging "%s" into "%s"' % (e, key, b, a))
    return a