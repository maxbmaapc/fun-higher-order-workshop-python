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
    have_been_called = False
    result = 0
    def inner_once(x):
        nonlocal have_been_called, result
        if not have_been_called:
            result = fn(x)
            have_been_called = True
            return result
        return None
    return inner_once

def twice(fn):
    return lambda x: fn(x, x)

def compose_u(f, g):
    return lambda x: g(f(x))

def compose_b(f, g):
    return lambda a, b, c: g(f(a, b), c)

def limit(fn, n):
    call_count = 0
    def inner_limit(a, b): 
       nonlocal call_count
       if call_count < n:
           call_count += 1
           return fn(a,b) 
       return None
    return inner_limit

def from_(start):
    count = start
    def inner_from():
       nonlocal count
       old_count = count
       count += 1
       return old_count
    return inner_from

def to(gen, end):
    def inner_to():
        count = gen()
        if count < end:
            return count
    return inner_to
def from_to(start, end):
    counter = start
    def inner_from_to():
        nonlocal counter
        if counter < end:
            old_count = counter
            counter += 1
            return old_count
    return inner_from_to

def element(lst, gen=None):
    count = 0
    def inner_element():
        nonlocal count
        counter = gen() if gen else None
        if counter:
            return lst[counter]
        elif gen == None:
            old_count = count
            count +=1
            if count <= len(lst):
               return lst[old_count] 
    return inner_element

def collect(gen, arr):
    def inner_collect():
        output = gen()

        if type(output) == int:
            arr.append(output)
            return output
    return inner_collect

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