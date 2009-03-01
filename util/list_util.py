def trim_if(l, test_func):
    """removes from start and end of list those values that match test_func
    
    >>> trim_if([1,2,3,1,2,3,1,2], lambda x: x < 3)
    [3, 1, 2, 3]
    >>> trim_if([1,2,1,2,1,2,1,2], lambda x: x < 3)
    []
    """
    start = 0
    end = len(l)
    for i, v in enumerate(l):
        if test_func(v):
            start = i+1
        else:
            break
    for i in xrange(end-1, start, -1):
        if test_func(l[i]):
            end = i
        else:
            break
    return l[start:end]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
