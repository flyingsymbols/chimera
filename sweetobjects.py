# intent here is to have a format that will handle storing to and from the
# users home directory as json, also clean to/from between basic python
# data structures (dict, list, int, float, str, etc)

from util.func_util import args_defaults_vars
from util.format_util import script_str

class SweetType(type):
    def __init__(cls, name, bases, curr_dict):
        type.__init__(cls, name, bases, curr_dict)
        if curr_dict.has_key('__init__'):
            a, d, v = args_defaults_vars(curr_dict['__init__'])
            attrs = a[1:] # skip self
            format_str = '%s(%s)' % (name,
                ', '.join('%s=%%r' for a in attrs))
            def new_repr(self):
                format_str % [getattr(self, a) for a in attrs]
                
            cls.__repr__ = new_repr


# introspection borrowed from ideas here:
# http://wordaligned.org/articles/echo

# want to be able to construct arbitrary Types such that
# they can be subcontained in ordered and unordered ways,
# they can be un-indexed or indexed by some arbitrary function
# temporary end-goal:
# want to be able to have a PostgresUser type that has
# username :: str
# password :: str
# superuser :: boolean
# databases :: defaultset([PostgresDatabase])

a = []


class SweetObject(object):
    __metaclass__ = SweetType

class PostgresUser(SweetObject):
    def __init__(self, username, password, superuser=False):
        a = 5
        b = 2
        
func_code = script_str("""
    def __init__(self, a, b, c = None):
        self.a = a
        self.b = b
        self.c = c
""")

