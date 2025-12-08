class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
if __name__ == '__main__':
    p = Point(1,2)
    print(p.x, p.y)
    try:
        p.z = 5
    except Exception as e:
        print(type(e).__name__)
