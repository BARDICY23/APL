def make_adder(n):
    def adder(x):
        return n + x
    return adder

add_5 = make_adder(5)
print(add_5(10))
print(add_5(3))
