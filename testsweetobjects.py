from sweetobjects import create_type
from nose.tools import assert_equal

@create_type
def Foo(a, b, c=50): pass

def test_basic():
    f = Foo(1, 2)
    f2 = Foo(b = 2, a = 1)
    f3 = Foo(1, 2, c = 50)
    f4 = Foo(1, 2, c = 3)
    assert f == f2
    assert f2 == f3
    assert f.a == 1
    assert f.b == 2
    assert f.c == 50
    assert f != f4
    assert f4.c == 3

def test_repl():
    f = Foo(1,2,3)
    assert_equal(repr(f), 'Foo(a=1,b=2,c=3)')
    assert f == eval(repr(f))


