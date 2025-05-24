# Fun Higher Order Workshop (Python)

This repository is inspired by [FunHigherOrderWorkshop](https://github.com/fuzzyJess/FunHigherOrderWorkshop) for JavaScript, but implemented in Python for daily practice.

## Goals

- Get comfortable with higher-order functions in Python (functions that receive other functions as arguments and/or return other functions)
- Practice TDD using pytest (tests included)
- Prepare for practical use of these patterns in real Python code

## Tasks

1. Write an `identity` function that takes an argument and returns that same argument.
2. Write a function `identity_f` that takes an argument and returns a function that returns that argument.
3. Write three binary functions, `add`, `subtract`, and `multiply` that take two numbers and return their sum, difference, and product respectively.
4. Write a function called `increment` that uses one of your previous functions to return a number incremented by 1.
5. Write a function `add_f` that adds from two invocations.
6. Write a function `curry` that takes a binary function and one argument, and returns a function that takes the second argument.
7. Write a function `lift_f` that takes a binary function and makes it callable with two invocations.
8. Write a function `once` that can only be called once.
9. Write a function `twice` that takes a binary function and returns a unary function that passes its argument to the binary function twice.
10. Write a function `compose_u` that takes two unary functions and returns a unary function that calls them both, in argument order.
11. Write a function `compose_b` that takes two binary functions and returns a function that calls them both. The return value of the first function will get passed as the first argument to the second one.
12. Write a `limit` function that allows a binary function to be called a limited number of times.
13. Write a `from_` function that produces a generator that will produce a series of consecutive numerical values starting from the argument passed.
14. Write a `to` function that takes a generator and an end value, and returns a generator that will produce numbers up to that limit (not inclusive).
15. Write a `from_to` function that produces a generator that will produce values in a range.
16. Write an `element` function that takes a list and a generator and returns a generator that will produce elements from the list.
17. Modify the `element` function so that the generator argument is optional. If a generator is not provided, then each of the elements of the list will be produced.
18. Write a `collect` function that takes a generator and a list and produces a function that will collect the results in the list by mutating it.
19. Write a `filter_` function that takes a generator and a predicate and produces a generator that produces only the values approved by the predicate.
20. Write a `concat` function that takes two generators and produces a generator that combines the sequences.
21. Make a function `fibonacci_f` that returns a generator that will return consecutive fibonacci numbers starting with the first two arguments.
22. Make a function `gen_sym_f` that makes a function that generates unique symbols.
23. Write a function `gen_sym_ff` that takes a unary function and a seed and returns a `gen_sym_f`.
24. Write a `counter` function that returns an object containing two functions that implement an up/down counter, hiding the counter value itself.
25. Write a `revokable` function that takes a binary function, and returns an object containing an `invoke` function that can invoke the binary function, and a `revoke` function that disables the `invoke` function.
26. Implement `curry` so that it works with any number of arguments.
27. Reimplement the `concat` function so that it will take any number of generators.

---

## How to use

- Implement each function in `workshop.py`.
- Run tests with `pytest`.

---

## License
MIT
