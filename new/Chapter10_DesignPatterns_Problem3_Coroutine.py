def filter_positive():
    while True:
        value = yield
        if value > 0:
            print(f"Positive number: {value}")

co = filter_positive()
next(co)
co.send(-3)
co.send(5)
co.send(0)
