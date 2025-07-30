#!/usr/bin/env python3
"""
Command-line interface for the Fun Higher Order Functions package.

This CLI provides interactive demonstrations and examples of the higher-order
functions available in the package.
"""

import argparse
import sys
from . import core


def demo_basic_functions():
    """Demonstrate basic functions."""
    print("=== Basic Functions Demo ===")
    print(f"identity(42): {core.identity(42)}")
    print(f"add(3, 4): {core.add(3, 4)}")
    print(f"subtract(10, 3): {core.subtract(10, 3)}")
    print(f"multiply(5, 6): {core.multiply(5, 6)}")
    print(f"increment(7): {core.increment(7)}")
    print()


def demo_higher_order_functions():
    """Demonstrate higher-order functions."""
    print("=== Higher-Order Functions Demo ===")
    
    # add_f demo
    add5 = core.add_f(5)
    print(f"add_f(5)(3): {add5(3)}")
    
    # curry demo
    multiply_by_10 = core.curry(core.multiply, 10)
    print(f"curry(multiply, 10)(4): {multiply_by_10(4)}")
    
    # once demo
    def greet(name):
        return f"Hello, {name}!"
    
    greet_once = core.once(greet)
    print(f"once(greet)('Alice'): {greet_once('Alice')}")
    print(f"once(greet)('Bob'): {greet_once('Bob')}")  # Should return None
    
    # twice demo
    double_add = core.twice(core.add)
    print(f"twice(add)(7): {double_add(7)}")  # 7 + 7 = 14
    print()


def demo_generators():
    """Demonstrate generator functions."""
    print("=== Generator Functions Demo ===")
    
    # from_ demo
    print("from_(5) generator:")
    counter = core.from_(5)
    for i in range(3):
        print(f"  {counter()}")
    
    # from_to demo
    print("from_to(0, 3) generator:")
    range_gen = core.from_to(0, 3)
    value = range_gen()
    while value is not None:
        print(f"  {value}")
        value = range_gen()
    
    # fibonacci demo
    print("fibonacci_f(0, 1) generator:")
    fib = core.fibonacci_f(0, 1)
    for i in range(6):
        print(f"  {fib()}")
    print()


def demo_symbol_generators():
    """Demonstrate symbol generator functions."""
    print("=== Symbol Generator Functions Demo ===")
    
    # gen_sym_f demo
    gen_a = core.gen_sym_f('A')
    gen_b = core.gen_sym_f('B')
    print("gen_sym_f('A') and gen_sym_f('B'):")
    for i in range(3):
        print(f"  A: {gen_a()}, B: {gen_b()}")
    print()


def demo_advanced_functions():
    """Demonstrate advanced functions."""
    print("=== Advanced Functions Demo ===")
    
    # counter demo
    print("counter(10) demo:")
    c = core.counter(10)
    print(f"  up(): {c['up']()}")     # 11
    print(f"  down(): {c['down']()}")  # 10
    print(f"  down(): {c['down']()}")  # 9
    print(f"  up(): {c['up']()}")     # 10
    
    # revokable demo
    print("revokable(add) demo:")
    rev_add = core.revokable(core.add)
    print(f"  invoke(3, 4): {rev_add['invoke'](3, 4)}")  # 7
    rev_add['revoke']()
    print(f"  invoke(5, 6) after revoke: {rev_add['invoke'](5, 6)}")  # None
    print()


def run_all_demos():
    """Run all demonstration functions."""
    print("Fun Higher Order Functions - Interactive Demo")
    print("=" * 50)
    print()
    
    demo_basic_functions()
    demo_higher_order_functions()
    demo_generators()
    demo_symbol_generators()
    demo_advanced_functions()
    
    print("Demo completed! Check out the source code for more details.")


def interactive_mode():
    """Run in interactive mode."""
    print("Fun Higher Order Functions - Interactive Mode")
    print("Type 'help' for available commands, 'quit' to exit.")
    print()
    
    while True:
        try:
            command = input(">>> ").strip().lower()
            
            if command in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            elif command in ['help', 'h']:
                print("Available commands:")
                print("  demo - Run all demonstrations")
                print("  basic - Demo basic functions")
                print("  higher - Demo higher-order functions")
                print("  generators - Demo generator functions")
                print("  symbols - Demo symbol generators")
                print("  advanced - Demo advanced functions")
                print("  help - Show this help")
                print("  quit - Exit interactive mode")
            elif command == 'demo':
                run_all_demos()
            elif command == 'basic':
                demo_basic_functions()
            elif command == 'higher':
                demo_higher_order_functions()
            elif command == 'generators':
                demo_generators()
            elif command == 'symbols':
                demo_symbol_generators()
            elif command == 'advanced':
                demo_advanced_functions()
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Fun Higher Order Functions CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  fun-higher-order demo          # Run all demonstrations
  fun-higher-order interactive   # Start interactive mode
  fun-higher-order --version     # Show version information
        """
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        choices=['demo', 'interactive'],
        default='demo',
        help='Command to run (default: demo)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Fun Higher Order Functions 1.0.0'
    )
    
    args = parser.parse_args()
    
    if args.command == 'demo':
        run_all_demos()
    elif args.command == 'interactive':
        interactive_mode()


if __name__ == '__main__':
    main()