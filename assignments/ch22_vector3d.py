class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
if __name__ == '__main__':
    a = Vector3D(1,2,3)
    b = Vector3D(4,5,6)
    print(a + b)
    print(a - b)
    print(a * b)
