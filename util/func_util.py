def args_defaults_vars(func):
    """get the arguments, defaults, and internal variables of a function

    >>> def foo(a, b, c, d=4): e = 1
    >>> args_defaults_vars(foo)
    (('a', 'b', 'c', 'd'), {'d': 4}, ('e',))
    """
    code = func.func_code
    count = code.co_argcount
    args = code.co_varnames[:count]
    def_vals = func.func_defaults or []
    defs = dict(zip(args[-len(def_vals):], def_vals))
    vars = code.co_varnames[count:]
    return args, defs, vars

if __name__ == '__main__':
    import doctest
    doctest.testmod()
