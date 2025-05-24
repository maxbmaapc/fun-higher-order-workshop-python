import pytest
import workshop

def test_identity():
    assert workshop.identity(5) == 5
    assert workshop.identity('a') == 'a'
    assert workshop.identity([1,2,3]) == [1,2,3]

def test_identity_f():
    f = workshop.identity_f(10)
    assert callable(f)
    assert f() == 10
    g = workshop.identity_f('hello')
    assert g() == 'hello'

def test_add():
    assert workshop.add(2, 3) == 5
    assert workshop.add(-1, 1) == 0
    assert workshop.add(0, 0) == 0

def test_subtract():
    assert workshop.subtract(5, 2) == 3
    assert workshop.subtract(2, 5) == -3
    assert workshop.subtract(0, 0) == 0

def test_multiply():
    assert workshop.multiply(3, 4) == 12
    assert workshop.multiply(-2, 3) == -6
    assert workshop.multiply(0, 100) == 0

def test_increment():
    assert workshop.increment(7) == 8
    assert workshop.increment(-1) == 0
    assert workshop.increment(0) == 1

def test_add_f():
    add3 = workshop.add_f(3)
    assert callable(add3)
    assert add3(4) == 7
    assert workshop.add_f(5)(6) == 11

def test_curry():
    add3 = workshop.curry(lambda a, b: a + b, 3)
    assert callable(add3)
    assert add3(4) == 7
    multiply5 = workshop.curry(lambda a, b: a * b, 5)
    assert multiply5(6) == 30

def test_lift_f():
    add_f = workshop.lift_f(lambda a, b: a + b)
    add3 = add_f(3)
    assert callable(add3)
    assert add3(4) == 7
    multiply_f = workshop.lift_f(lambda a, b: a * b)
    multiply5 = multiply_f(5)
    assert multiply5(6) == 30

def test_once():
    called = []
    def fn(x):
        called.append(x)
        return x
    once_fn = workshop.once(fn)
    assert once_fn(5) == 5
    assert once_fn(10) is None
    assert called == [5]

def test_twice():
    double = workshop.twice(lambda a, b: a + b)
    assert double(11) == 22
    square = workshop.twice(lambda a, b: a * b)
    assert square(11) == 121

def test_compose_u():
    double = lambda a: a * 2
    square = lambda a: a ** 2
    assert workshop.compose_u(double, square)(5) == 100
    assert workshop.compose_u(square, double)(5) == 50

def test_compose_b():
    def add(a, b): return a + b
    def multiply(a, b): return a * b
    assert workshop.compose_b(add, multiply)(2, 3, 7) == 35
    assert workshop.compose_b(multiply, add)(2, 3, 7) == 13

def test_limit():
    add_ltd = workshop.limit(lambda a, b: a + b, 1)
    assert add_ltd(3, 4) == 7
    assert add_ltd(3, 5) is None
    add_ltd2 = workshop.limit(lambda a, b: a + b, 2)
    assert add_ltd2(1, 2) == 3
    assert add_ltd2(2, 3) == 5
    assert add_ltd2(3, 4) is None

def test_from_():
    index = workshop.from_(0)
    assert index() == 0
    assert index() == 1
    assert index() == 2
    index2 = workshop.from_(5)
    assert index2() == 5
    assert index2() == 6

def test_to():
    index = workshop.to(workshop.from_(1), 3)
    assert index() == 1
    assert index() == 2
    assert index() is None

def test_from_to():
    index = workshop.from_to(0, 3)
    assert index() == 0
    assert index() == 1
    assert index() == 2
    assert index() is None
    index2 = workshop.from_to(2, 2)
    assert index2() is None

def test_element():
    ele = workshop.element(['a', 'b', 'c', 'd'], workshop.from_to(1, 3))
    assert ele() == 'b'
    assert ele() == 'c'
    assert ele() is None
    ele2 = workshop.element(['a', 'b', 'c', 'd'])
    assert ele2() == 'a'
    assert ele2() == 'b'
    assert ele2() == 'c'
    assert ele2() == 'd'
    assert ele2() is None
    ele3 = workshop.element([], workshop.from_to(0, 1))
    assert ele3() is None

def test_collect():
    arr = []
    col = workshop.collect(workshop.from_to(0, 2), arr)
    assert col() == 0
    assert col() == 1
    assert col() is None
    assert arr == [0, 1]
    arr2 = [10]
    col2 = workshop.collect(workshop.from_to(1, 3), arr2)
    assert col2() == 1
    assert col2() == 2
    assert col2() is None
    assert arr2 == [10, 1, 2]

def test_filter_():
    def third(value):
        return value % 3 == 0
    fil = workshop.filter_(workshop.from_to(0, 5), third)
    assert fil() == 0
    assert fil() == 3
    assert fil() is None
    fil2 = workshop.filter_(workshop.from_to(1, 4), lambda x: x > 2)
    assert fil2() == 3
    assert fil2() is None

def test_concat():
    con = workshop.concat(workshop.from_to(0, 3), workshop.from_to(0, 2))
    assert con() == 0
    assert con() == 1
    assert con() == 2
    assert con() == 0
    assert con() == 1
    assert con() is None
    con2 = workshop.concat(lambda: None, lambda: None)
    assert con2() is None

def test_fibonacci_f():
    fib = workshop.fibonacci_f(0, 1)
    assert fib() == 0
    assert fib() == 1
    assert fib() == 1
    assert fib() == 2
    assert fib() == 3
    assert fib() == 5
    fib2 = workshop.fibonacci_f(2, 3)
    assert fib2() == 2
    assert fib2() == 3
    assert fib2() == 5
    assert fib2() == 8

def test_gen_sym_f():
    gen_g = workshop.gen_sym_f('G')
    gen_h = workshop.gen_sym_f('H')
    assert gen_g() == 'G0'
    assert gen_h() == 'H0'
    assert gen_g() == 'G1'
    assert gen_h() == 'H1'
    assert gen_g() == 'G2'
    assert gen_h() == 'H2'

def test_gen_sym_ff():
    def inc(x):
        return x + 1
    gen_sym_f = workshop.gen_sym_ff(inc, 0)
    gen_g = gen_sym_f('G')
    gen_h = gen_sym_f('H')
    assert gen_g() == 'G1'
    assert gen_h() == 'H1'
    assert gen_g() == 'G2'
    assert gen_h() == 'H2'

def test_counter():
    obj = workshop.counter(10)
    up = obj['up']
    down = obj['down']
    assert up() == 11
    assert down() == 10
    assert down() == 9
    assert up() == 10

def test_revokable():
    def add(a, b):
        return a + b
    rev = workshop.revokable(add)
    assert rev['invoke'](3, 4) == 7
    rev['revoke']()
    assert rev['invoke'](5, 7) is None
