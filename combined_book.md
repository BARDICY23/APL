[//]: # (Combined document generated from `book.md` and `assignments/`)
# Advanced Programming With Python — Combined Notes and Assignments

This document consolidates the formatted `book.md` content and all files from `assignments/` into one structured markdown file. Use this as the source to convert to PDF.

---

## Table of Contents

- Book Notes (original `book.md`)
- Assignments README
- Chapter 3: Functions and ETL
- Chapter 4: Regex
- Chapter 5: OOP
- Chapter 6: I/O (CSV/JSON/Excel)
- Chapter 7: Databases (SQLite & SQLAlchemy)
- Chapter 8: NumPy / Pandas / Matplotlib / PyTorch
- Chapter 9: Web Scraping & Selenium
- Chapter 10: Contexts, Generators, Patterns
- Chapter 11: Reflections and Written Answers
- Chapter 22: Data Model (Vector, Descriptor, Slots)
- Answer Key & Requirements

---

## Book Notes (book.md)

```markdown
# Advanced Programming With Python — Notes (Formatted)

Here is the content of the PDF in a single plaintext format, cleaned and structured for readability. All original content is preserved.

---

## Chapter 11.11 — Review Questions

To reinforce your understanding of the concepts introduced in this chapter, attempt the following exercises. These practical tasks will help you apply the theoretical knowledge of Python's philosophy, execution model, and dynamic nature.

### The Zen of Python — Reflection

- Open a Python interpreter and type `import this`.
- Read through "The Zen of Python" and select three principles that resonate most with your coding philosophy or that you find particularly insightful.

DR. HEND SHAABAN 21

**Write:** A short explanation (1–2 paragraphs per principle) of how each chosen principle might guide your coding style and decision-making in advanced Python projects.

### Bytecode Inspection

- Define a Python function `square(x)` that returns the square of its input `x` (i.e., `x*x`).
- Use the `dis` module (`import dis; dis.dis(square)`) to inspect its bytecode.
- Identify which bytecode instructions correspond to the multiplication operation. How does this compare to the `BINARY_ADD` instruction seen in the `add` function example?
- Now, define a function `multiply(a, b)` that returns the product of `a` and `b`. Disassemble its bytecode and compare it with the `add()` function example from the chapter. Note any similarities or differences in the bytecode instructions for arithmetic operations.

### Dynamic Typing in Action

- Create a variable named `data`.
- Assign an integer value to `data` and print its type using `type(data)`.
- Reassign `data` to a list and print its type again.
- Finally, reassign `data` to a simple function (e.g., `def my_func(): pass`) and print its type.
- Reflect on what this sequence of operations reveals about how Python handles variable types compared to statically typed languages.

### Comparing Python Implementations

- Conduct brief research on PyPy and Jython (if you haven't already).
- In a short note (approximately 3–4 sentences for each), explain how PyPy and Jython differ from CPython.
- Describe specific scenarios or use cases where each alternative implementation (PyPy and Jython) might be more advantageous than CPython.

DR. HEND SHAABAN 22

### Abstract Syntax Tree (AST) Exploration

- Using the `ast` module, parse the following Python code snippet:

```python
y = (4*5) - 3
```

- Print the AST using `ast.dump(tree, indent=4)`.
- From the printed AST, identify the specific AST nodes that represent the multiplication operation `(4*5)` and the subtraction operation `(... - 3)`. How are binary operations structured within the AST?

### Mutability and Object Identity

- Create a Python list, for example, `my_list = [10, 20, 30]`.
- Print the memory address (identity) of `my_list` using `id(my_list)`.
- Append a new value to the list (e.g., `my_list.append(40)`).
- Print the memory address of `my_list` again.
- Compare the two memory addresses. What does this observation reveal about the mutability of lists in Python and how changes to mutable objects affect their identity in memory?

---

## Chapter 22.5 — Review Questions

To consolidate your understanding of the Python Data Model and Internals, work through the following exercises. These problems are designed to help you apply the concepts of object identity, mutability, hashability, special methods, descriptors, and slots.

1. **Vector3D Class with Operator Overloading**

   - Create a class `Vector3D` that represents a 3-dimensional vector with `x`, `y`, and `z` components.
   - Implement the `__init__` method to initialize these components.
   - Overload the addition operator (`+`) using `__add__` so that two `Vector3D` objects can be added component-wise.
   - Overload the subtraction operator (`-`) using `__sub__` for component-wise subtraction.

DR HEND SHAABAN 36

   - Overload the multiplication operator (`*`) using `__mul__` to calculate the dot product of two `Vector3D` objects.
   - Implement `__repr__` for a clear string representation of `Vector3D` objects.
   - Test your `Vector3D` class with various operations.

2. **Positive Number Descriptor**

   - Create a descriptor class named `Positive`.
   - This descriptor should ensure that any attribute it manages can only be set to a non-negative number (zero or positive).
   - If an attempt is made to set a negative value, it should raise a `ValueError`.
   - Apply this `Positive` descriptor to a `balance` attribute in a `BankAccount` class to ensure the balance never goes below zero (without an overdraft).

3. **Point Class with `__slots__`**

   - Define a class `Point` that represents a 2D point with `x` and `y` coordinates.
   - Use `__slots__` to restrict its attributes to only `x` and `y`.
   - Create an instance of `Point` and assign values to `x` and `y`.
   - Attempt to add a third attribute (e.g., `p.z = 5`) to an instance of `Point`.
   - Explain what happens and why, relating it back to the purpose of `__slots__`.

4. **Disassembling a Simple Function**

   - Define a simple Python function, for example:

```python
def calculate_sum(a, b):
	return a + b
```

   - Use the `dis` module (`import dis; dis.dis(calculate_sum)`) to disassemble this function.
   - Analyze the bytecode instructions. What do `LOAD_FAST`, `BINARY_ADD`, and `RETURN_VALUE` signify in the context of Python's execution model?
   - How does this relate to the stack-based nature of the PVM?

---

## Chapter 3 — Exercises

1. Write a pure function `remove_vowels(text)` that takes a string and returns a new string with all vowels removed.
2. Given a list of numbers, use `map()` and `filter()` to create a new list containing the squares of only the odd numbers.
3. Implement a recursive function to calculate the `n`th Fibonacci number. Use `functools.lru_cache` to memoize the results and compare its performance.
4. Write a closure `make_adder(n)` that returns a function. The returned function should take a number `x` and return `n+x`.
5. Implement a higher-order function `apply_twice(func, value)` that applies a given function `func` to a value twice (e.g., `apply_twice(lambda x: x+1, 5)` should return `7`).
6. Build a functional ETL pipeline that takes a list of strings, tokenizes them into words, removes common "stopwords" (e.g., "the", "a", "is"), and returns a dictionary with the frequency of each remaining word.
7. Challenge: Implement your own version of the `reduce()` function.
8. Create a decorator `log_call(func)` that logs a message to the console before and after calling the decorated function.

ADVANCED PROGRAMMING WITH PYTHON

---

## Chapter 3.15 — Review Questions (Functional Programming)

### Multiple Choice Questions (MCQs)

9. Which of the following is a characteristic of a pure function?
   a) Depends on global variables
   b) Produces side effects
   c) Always returns the same output for the same input
   d) Modifies input arguments

10. Which functional programming concept ensures that once a variable is assigned, it cannot be changed?
   a) Recursion
   b) Immutability
   c) Closures
   d) Memoization

11. Which built-in function applies a function to all elements of an iterable and returns an iterator?
   a) `filter()`
   b) `reduce()`
   c) `map()`
   d) `zip()`

12. Which module provides the `reduce` function in Python?
   a) `operator`
   b) `itertools`
   c) `functools`
   d) `collections`

13. The `filter()` function in Python returns:
   a) A list of all elements
   b) An iterator containing elements that satisfy the condition
   c) A tuple of matching elements
   d) None

DR. HEND SHAABAN 55

ADVANCED PROGRAMMING WITH PYTHON

### True/False Questions

14. Functional programming in Python encourages immutability and pure functions.
15. The `map()` function modifies the original iterable in place.
16. Closures allow inner functions to access variables from their enclosing function even after the outer function has finished execution.
17. The `reduce()` function is a built-in function in Python and does not require an import.
18. `itertools` provide memory-efficient tools for working with iterators, including infinite sequences.

---

## Assignments README

```markdown
This folder contains implementations for the programming tasks listed in the formatted book.md.

Files:
- ch10_timer.py: Timer context manager example
- ch10_even_numbers.py: Generator of even numbers
- ch10_filter_positive.py: Coroutine that filters positive numbers
- ch10_factory_observer.py: Factory and Observer pattern examples
- ch22_vector3d.py: Vector3D implementation
- ch22_positive_descriptor.py: Positive descriptor + BankAccount
- ch22_point_slots.py: Point class using __slots__
- ch3_functions.py: functional programming utilities (no comments)
- ch3_etl.py: simple ETL pipeline using regex tokenization
- ch4_regex.py: regex exercises implementations
- ch5_oop.py: Rectangle, Employee, Vehicle, Vector, print_shape_area
- ch6_io.py: CSV, JSON, Excel helpers
- ch7_sqlite.py: sqlite CRUD and transaction example
- ch7_sqlalchemy.py: SQLAlchemy ORM Book example
- ch8_numpy_pandas.py: NumPy and Pandas tasks
- ch8_matplotlib.py: Matplotlib sample plot saved to sample_plot.png
- ch8_pytorch.py: PyTorch tensor operations
- ch9_scraping.py: requests + BeautifulSoup scraping helpers
- ch9_selenium_google.py: Selenium Google search script (requires webdriver)

Run individual files with Python to try examples. Install dependencies listed in requirements.txt if needed.

```

---

## Chapter 3: Functional Code (`ch3_functions.py`)

```python
from functools import lru_cache
def remove_vowels(text):
	return ''.join(ch for ch in text if ch.lower() not in 'aeiou')
def odd_squares(nums):
	return list(map(lambda x: x*x, filter(lambda x: x%2==1, nums)))
@lru_cache(maxsize=None)
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)
def make_adder(n):
	def adder(x):
		return n + x
	return adder
def apply_twice(func, value):
	return func(func(value))
def my_reduce(func, iterable, initial=None):
	it = iter(iterable)
	if initial is None:
		try:
			value = next(it)
		except StopIteration:
			raise TypeError('reduce() of empty sequence with no initial value')
	else:
		value = initial
	for x in it:
		value = func(value, x)
	return value
def log_call(func):
	def wrapper(*args, **kwargs):
		print(f"Calling {func.__name__}")
		res = func(*args, **kwargs)
		print(f"Finished {func.__name__}")
		return res
	return wrapper
if __name__ == '__main__':
	print(remove_vowels('Hello World'))
	print(odd_squares([1,2,3,4,5]))
	print(fib(10))
	add5 = make_adder(5)
	print(add5(3))
	print(apply_twice(lambda x: x+1, 5))
	print(my_reduce(lambda a,b: a+b, [1,2,3,4]))
	@log_call
	def greet(name):
		return f"Hello {name}"
	print(greet('Alice'))

```

