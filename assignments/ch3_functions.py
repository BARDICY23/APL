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
