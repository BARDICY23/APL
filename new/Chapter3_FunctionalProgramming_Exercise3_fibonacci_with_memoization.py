from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

def fib_no_memo(n):
    if n <= 1:
        return n
    return fib_no_memo(n-1) + fib_no_memo(n-2)

start = time.time()
print(f"With memoization: {fib_memo(35)}")
print(f"Time: {time.time() - start}")

start = time.time()
print(f"Without memoization: {fib_no_memo(30)}")
print(f"Time: {time.time() - start}")
