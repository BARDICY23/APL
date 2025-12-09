class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(f"x: {p.x}, y: {p.y}")

try:
    p.z = 5
except AttributeError as e:
    print(f"Error: {e}")
