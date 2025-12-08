class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    @classmethod
    def from_string(cls, s):
        parts = s.split(',')
        return cls(parts[0], parts[1], float(parts[2]))
    def display_employee_info(self):
        print(self.name, self.employee_id, self.salary)
class Vehicle:
    def move(self):
        print('Vehicle is moving')
class Car(Vehicle):
    def move(self):
        print('Car is driving')
class Bike(Vehicle):
    def move(self):
        print('Bike is cycling')
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
def print_shape_area(shape):
    print(shape.area())
if __name__ == '__main__':
    r = Rectangle(3,4)
    print(r.area(), r.perimeter())
    e = Employee.from_string('John Doe,E123,50000')
    e.display_employee_info()
    v = [Car(), Bike(), Vehicle()]
    for obj in v:
        obj.move()
    a = Vector(1,2)
    b = Vector(3,4)
    print(a - b)
    print(a * b)
    class Circle:
        def __init__(self, r):
            self.r = r
        def area(self):
            return 3.14159 * self.r * self.r
    print_shape_area(Circle(2))
