class Positive:
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name, 0)
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Value must be non-negative')
        setattr(instance, self.name, value)
class BankAccount:
    balance = Positive()
    def __init__(self, balance=0):
        self.balance = balance
if __name__ == '__main__':
    a = BankAccount(100)
    print(a.balance)
    try:
        a.balance = -50
    except Exception as e:
        print(e)
