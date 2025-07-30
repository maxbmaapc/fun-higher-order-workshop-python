"""
Fun Higher Order Functions Package

A collection of higher-order functions for functional programming in Python.
This package provides utilities for function composition, currying, generators,
and other functional programming patterns.
"""

from .core import *

__version__ = "1.0.0"
__author__ = "Fun Higher Order Workshop"
__email__ = "workshop@example.com"
__description__ = "Higher-order functions toolkit for Python"

__all__ = [
    # Basic functions
    'identity', 'identity_f',
    'add', 'subtract', 'multiply', 'increment',
    
    # Higher-order functions
    'add_f', 'curry', 'lift_f', 'once', 'twice',
    'compose_u', 'compose_b', 'limit',
    
    # Generators
    'from_', 'to', 'from_to', 'element', 'collect',
    'filter_', 'concat', 'fibonacci_f',
    
    # Symbol generators
    'gen_sym_f', 'gen_sym_ff',
    
    # Advanced functions
    'counter', 'revokable'
]