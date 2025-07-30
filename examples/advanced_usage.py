#!/usr/bin/env python3
"""
Advanced usage examples for the Fun Higher Order Functions package.

This file demonstrates advanced patterns using generators, composition,
and other sophisticated higher-order functions.
"""

import sys
import os

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fun_higher_order import *


def composition_examples():
    """Examples of function composition."""
    print("=== Function Composition Examples ===")
    
    # Compose unary functions
    double = lambda x: x * 2
    square = lambda x: x ** 2
    
    # First double, then square
    double_then_square = compose_u(double, square)
    print(f"compose_u(double, square)(3): {double_then_square(3)}")  # (3*2)^2 = 36
    
    # First square, then double
    square_then_double = compose_u(square, double)
    print(f"compose_u(square, double)(3): {square_then_double(3)}")  # (3^2)*2 = 18
    
    # Compose binary functions
    result = compose_b(add, multiply)(2, 3, 4)  # (2+3)*4 = 20
    print(f"compose_b(add, multiply)(2, 3, 4): {result}")


def generator_examples():
    """Examples of generator functions."""
    print("\n=== Generator Examples ===")
    
    # Create a range of numbers
    print("Numbers from 0 to 4:")
    counter = from_to(0, 5)
    numbers = []
    value = counter()
    while value is not None:
        numbers.append(value)
        value = counter()
    print(f"  {numbers}")
    
    # Filter even numbers
    print("Even numbers from 0 to 9:")
    even_filter = filter_(from_to(0, 10), lambda x: x % 2 == 0)
    evens = []
    value = even_filter()
    while value is not None:
        evens.append(value)
        value = even_filter()
    print(f"  {evens}")
    
    # Concatenate two sequences
    print("Concatenating [0,1,2] and [10,11]:")
    concat_gen = concat(from_to(0, 3), from_to(10, 12))
    concat_result = []
    value = concat_gen()
    while value is not None:
        concat_result.append(value)
        value = concat_gen()
    print(f"  {concat_result}")
    
    # Fibonacci sequence
    print("First 8 Fibonacci numbers:")
    fib = fibonacci_f(0, 1)
    fibonacci_sequence = [fib() for _ in range(8)]
    print(f"  {fibonacci_sequence}")


def practical_examples():
    """Practical real-world examples."""
    print("\n=== Practical Examples ===")
    
    # Rate limiting with limit function
    print("Rate-limited API calls:")
    def api_call(endpoint, data):
        return f"Called {endpoint} with {data}"
    
    limited_api = limit(api_call, 3)  # Only allow 3 calls
    
    for i in range(5):
        result = limited_api(f"/api/v{i}", f"data_{i}")
        if result:
            print(f"  Call {i+1}: {result}")
        else:
            print(f"  Call {i+1}: Rate limit exceeded")
    
    # Counter for tracking operations
    print("\nOperation counter:")
    op_counter = counter(0)
    
    print(f"  Start: {op_counter['up']()}")  # 1
    print(f"  Process: {op_counter['up']()}")  # 2
    print(f"  Complete: {op_counter['up']()}")  # 3
    print(f"  Undo: {op_counter['down']()}")  # 2
    
    # Revokable access control
    print("\nRevokable access control:")
    def secure_operation(user, action):
        return f"User {user} performed {action}"
    
    access_control = revokable(secure_operation)
    
    print(f"  Before revoke: {access_control['invoke']('Alice', 'read')}")
    access_control['revoke']()
    print(f"  After revoke: {access_control['invoke']('Alice', 'write')}")


def symbol_generator_examples():
    """Examples of symbol generators."""
    print("\n=== Symbol Generator Examples ===")
    
    # Generate unique identifiers
    id_gen = gen_sym_f('ID')
    user_gen = gen_sym_f('USER')
    
    print("Generating unique IDs:")
    for _ in range(3):
        print(f"  ID: {id_gen()}, User: {user_gen()}")
    
    # Custom symbol generator with transformation
    def double(x):
        return x * 2
    
    custom_gen_factory = gen_sym_ff(double, 1)
    custom_gen = custom_gen_factory('CUSTOM')
    
    print("Custom generator with doubling:")
    for _ in range(3):
        print(f"  {custom_gen()}")


def main():
    """Run all advanced examples."""
    composition_examples()
    generator_examples()
    practical_examples()
    symbol_generator_examples()
    
    print("\n=== Summary ===")
    print("These examples show how higher-order functions can be used to:")
    print("- Create reusable, composable code")
    print("- Implement functional programming patterns")
    print("- Build generators and iterators")
    print("- Control function execution (rate limiting, access control)")
    print("- Generate unique identifiers and symbols")


if __name__ == '__main__':
    main()