class Vector:
    def __init__(self, values):
        self.values = values
    
    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.values, other.values)])
    
    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.values, other.values))

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(f"Subtraction: {(v1 - v2).values}")
print(f"Dot Product: {v1 * v2}")
