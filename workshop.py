"""
Fun Higher Order Workshop (Python)
Implement each function below for daily practice.
"""

def identity(x):
    return x

def identity_f(x):
    return lambda: x

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def increment(x):
    return x + 1

def add_f(x):
    return lambda y: x + y

def curry(fn, x):
    return lambda y: fn(x, y)

def lift_f(fn):
    return lambda n1: lambda n2: fn(n1, n2)

def once(fn):
    pass

def twice(fn):
    pass

def compose_u(f, g):
    pass

def compose_b(f, g):
    pass

def limit(fn, n):
    pass

def from_(start):
    pass

def to(gen, end):
    pass

def from_to(start, end):
    pass

def element(lst, gen=None):
    pass

def collect(gen, arr):
    pass

def filter_(gen, predicate):
    pass

def concat(gen1, gen2):
    pass

def fibonacci_f(a, b):
    pass

def gen_sym_f(prefix):
    pass

def gen_sym_ff(unary_fn, seed):
    pass

def counter(x):
    pass

def revokable(fn):
    pass
# Advanced tasks left for you to implement!