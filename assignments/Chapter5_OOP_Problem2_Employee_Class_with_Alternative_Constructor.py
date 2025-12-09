class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    @classmethod
    def from_string(cls, employee_str):
        parts = employee_str.split(',')
        return cls(parts[0], parts[1], float(parts[2]))
    
    def display_employee_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

emp = Employee.from_string("John Doe,E123,50000")
emp.display_employee_info()
