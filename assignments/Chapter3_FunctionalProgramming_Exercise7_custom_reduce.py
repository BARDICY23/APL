from functools import reduce as functools_reduce

def reduce(func, iterable, initial=None):
    iterator = iter(iterable)
    if initial is None:
        try:
            accumulator = next(iterator)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value")
    else:
        accumulator = initial
    
    for value in iterator:
        accumulator = func(accumulator, value)
    
    return accumulator

result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(result)
