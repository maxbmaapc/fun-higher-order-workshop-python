#!/usr/bin/env python3
"""
Basic usage examples for the Fun Higher Order Functions package.

This file demonstrates how to use the basic functions in the package.
"""

import sys
import os

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fun_higher_order import *


def main():
    print("=== Basic Functions Examples ===")
    
    # Identity function
    print(f"identity(42): {identity(42)}")
    print(f"identity('hello'): {identity('hello')}")
    
    # Basic arithmetic
    print(f"add(3, 4): {add(3, 4)}")
    print(f"subtract(10, 3): {subtract(10, 3)}")
    print(f"multiply(5, 6): {multiply(5, 6)}")
    print(f"increment(7): {increment(7)}")
    
    print("\n=== Higher-Order Functions Examples ===")
    
    # Function that returns a function
    identity_func = identity_f(100)
    print(f"identity_f(100)(): {identity_func()}")
    
    # Partial application
    add10 = add_f(10)
    print(f"add_f(10)(5): {add10(5)}")
    
    # Currying
    multiply_by_3 = curry(multiply, 3)
    print(f"curry(multiply, 3)(4): {multiply_by_3(4)}")
    
    # Lifting binary functions
    lifted_add = lift_f(add)
    add7 = lifted_add(7)
    print(f"lift_f(add)(7)(3): {add7(3)}")
    
    # Function that can only be called once
    def expensive_operation(x):
        print(f"  Performing expensive operation on {x}")
        return x * 2
    
    once_func = once(expensive_operation)
    print(f"once(expensive_operation)(5): {once_func(5)}")
    print(f"once(expensive_operation)(10): {once_func(10)}")  # Should return None
    
    # Function that calls binary function with same argument twice
    double_add = twice(add)
    print(f"twice(add)(6): {double_add(6)}")  # 6 + 6 = 12
    
    square = twice(multiply)
    print(f"twice(multiply)(5): {square(5)}")  # 5 * 5 = 25


if __name__ == '__main__':
    main()