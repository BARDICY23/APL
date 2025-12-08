def filter_positive():
    try:
        while True:
            x = (yield)
            if x > 0:
                print(f"Positive number: {x}")
    except GeneratorExit:
        return
if __name__ == '__main__':
    co = filter_positive()
    next(co)
    co.send(-3)
    co.send(5)
    co.send(0)
    co.close()
