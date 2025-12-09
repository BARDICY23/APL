class Positive:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} cannot be negative")
        obj.__dict__[self.name] = value

class BankAccount:
    balance = Positive('balance')
    
    def __init__(self, initial_balance):
        self.balance = initial_balance

account = BankAccount(100)
print(account.balance)
account.balance = 50
print(account.balance)
