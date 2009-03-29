# intent here is to have a format that will handle storing to and from the
# users home directory as json, also clean to/from between basic python
# data structures (dict, list, int, float, str, etc)

# implemented as a decorator over functions
# don't need to show defaults... but defaults can change

class SweetObject(object): # placeholder
    pass

from util.func_util import args_defaults_vars
from util.format_util import script_str

def create_type(f):
    args, defaults, v = args_defaults_vars(f)
    class_name = f.__name__
    if globals().has_key(class_name):
        raise TypeError, '%s already exists' % (class_name,)
    positionals = args[0:-len(defaults)]
    keywords = args[-len(defaults):]
    total = len(args)

    class klass(SweetObject):
        def __init__(self, *pvals, **kwvals):
            if len(kwvals) + len(pvals) > total:
                raise TypeError, "Invalid number of parameters"
            else:
                self.__dict__ = dict(zip(args, pvals))
            for n,v in kwvals.iteritems():
                if n in args:
                    self.__dict__[n] = v
                else:
                    raise TypeError, \
                        'Invalid keyword parameter %r' % (name,)
            for n,v in defaults.iteritems():
                if n not in self.__dict__:
                    self.__dict__[n] = v

        def __repr__(self):
            param_str = ','.join(['%s=%r' % (n, self.__dict__[n])
                for n in args])
            return '%s(%s)' % (self.__class__.__name__, param_str)

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

    klass.__name__ = class_name
    return klass







