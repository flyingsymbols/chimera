import re

from list_util import trim_if

script_str_test1 = """
    def __init__(self, a, b, c):
        self.a = a
        self.foo = (b, c)
    """

def script_str(s):
    """used to take triple quoted strings and make them indent compatible
    
    >>> print script_str_test1
    <BLANKLINE>
        def __init__(self, a, b, c):
            self.a = a
            self.foo = (b, c)
    <BLANKLINE>
    >>> print script_str(script_str_test1)
    def __init__(self, a, b, c):
        self.a = a
        self.foo = (b, c)
    """
    lines = [l.rstrip() for l in s.split('\n')]
    lines = trim_if(lines, lambda l: l == '') 
    first_l = lines[0]
    first_ws = first_l[:-len(first_l.lstrip())]
    def strip_ws(line):
        if line.startswith(first_ws):
            return line[len(first_ws):]
        elif line == '':
            return line
        else:
            raise TypeError, 'script_str whitespace mismatch'
    return '\n'.join(strip_ws(l) for l in lines)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
