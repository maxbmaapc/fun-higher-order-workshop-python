# Fun Higher Order Functions (Python)

A complete Python package for functional programming with higher-order functions. This package provides a comprehensive toolkit of functions for composition, currying, generators, and other functional programming patterns.

## Features

- **Basic Functions**: Identity, arithmetic operations, and utilities
- **Higher-Order Functions**: Currying, function composition, and lifting
- **Generators**: Flexible sequence generation with filtering and concatenation
- **Advanced Patterns**: Rate limiting, access control, and symbol generation
- **CLI Interface**: Interactive demonstrations and examples
- **Complete Test Suite**: 100% test coverage with pytest

## Installation

### From Source

```bash
git clone https://github.com/maxbmaapc/fun-higher-order-workshop-python.git
cd fun-higher-order-workshop-python
pip install -e .
```

### For Development

```bash
git clone https://github.com/maxbmaapc/fun-higher-order-workshop-python.git
cd fun-higher-order-workshop-python
pip install -e ".[dev]"
```

## Quick Start

### Using as a Library

```python
from fun_higher_order import *

# Basic usage
result = add(3, 4)  # 7
doubled = twice(multiply)(5)  # 5 * 5 = 25

# Higher-order functions
add10 = add_f(10)
result = add10(5)  # 15

# Generators
counter = from_to(0, 5)
numbers = []
value = counter()
while value is not None:
    numbers.append(value)
    value = counter()
print(numbers)  # [0, 1, 2, 3, 4]

# Fibonacci sequence
fib = fibonacci_f(0, 1)
sequence = [fib() for _ in range(8)]
print(sequence)  # [0, 1, 1, 2, 3, 5, 8, 13]
```

### Using the CLI

```bash
# Run interactive demonstrations
fun-higher-order demo

# Start interactive mode
fun-higher-order interactive

# Show version
fun-higher-order --version
```

## Available Functions

### Basic Functions
- `identity(x)` - Returns the argument unchanged
- `identity_f(x)` - Returns a function that returns the argument
- `add(a, b)`, `subtract(a, b)`, `multiply(a, b)` - Basic arithmetic
- `increment(x)` - Increments a number by 1

### Higher-Order Functions
- `add_f(x)` - Partial application of addition
- `curry(fn, x)` - Curries a binary function with one argument
- `lift_f(fn)` - Lifts a binary function to work with currying
- `once(fn)` - Creates a function that can only be called once
- `twice(fn)` - Creates a function that calls a binary function with the same argument twice
- `compose_u(f, g)` - Composes two unary functions
- `compose_b(f, g)` - Composes two binary functions
- `limit(fn, n)` - Limits the number of times a function can be called

### Generators
- `from_(start)` - Creates a counter starting from a value
- `to(gen, end)` - Limits a generator to produce values up to an end value
- `from_to(start, end)` - Creates a range generator
- `element(lst, gen=None)` - Creates a generator that produces elements from a list
- `collect(gen, arr)` - Collects generator values into an array
- `filter_(gen, predicate)` - Filters generator values with a predicate
- `concat(gen1, gen2)` - Concatenates two generators
- `fibonacci_f(a, b)` - Creates a Fibonacci sequence generator

### Symbol Generators
- `gen_sym_f(prefix)` - Creates a symbol generator with a prefix
- `gen_sym_ff(unary_fn, seed)` - Creates a customizable symbol generator factory

### Advanced Functions
- `counter(x)` - Creates an up/down counter object
- `revokable(fn)` - Creates a revokable function wrapper

## Examples

Check out the `examples/` directory for comprehensive usage examples:

- `examples/basic_usage.py` - Basic function usage and patterns
- `examples/advanced_usage.py` - Advanced patterns and real-world examples

```bash
# Run the examples
python examples/basic_usage.py
python examples/advanced_usage.py
```

## Development

### Running Tests

```bash
pytest                          # Run all tests
pytest -v                       # Verbose output
pytest --cov=fun_higher_order   # With coverage report
```

### Code Quality

```bash
black fun_higher_order/         # Format code
flake8 fun_higher_order/        # Lint code
```

## Goals

This package is designed to help you:

- **Get comfortable with higher-order functions** in Python (functions that receive other functions as arguments and/or return other functions)
- **Practice functional programming patterns** with real, tested implementations
- **Prepare for practical use** of these patterns in production Python code
- **Learn by example** with comprehensive documentation and demonstrations

## Use Cases

- **Functional Programming**: Build composable, reusable functions
- **Data Processing**: Create flexible pipelines with generators and filters
- **Rate Limiting**: Control function execution frequency
- **Caching**: Implement once-only execution patterns
- **Symbol Generation**: Generate unique identifiers and symbols
- **Educational**: Learn functional programming concepts interactively

## Architecture

```
fun_higher_order/
├── __init__.py          # Package exports and metadata
├── core.py              # Core function implementations
└── cli.py               # Command-line interface

examples/
├── basic_usage.py       # Basic usage examples
└── advanced_usage.py    # Advanced patterns and real-world examples

tests/
└── test_workshop.py     # Comprehensive test suite
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

This project transforms a functional programming workshop into a complete, production-ready Python package with CLI interface, comprehensive examples, and proper packaging.
