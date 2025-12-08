class Circle:
    def draw(self):
        print("Drawing a Circle")
class Square:
    def draw(self):
        print("Drawing a Square")
def shape_factory(name):
    n = name.lower()
    if n == 'circle':
        return Circle()
    if n == 'square':
        return Square()
    raise ValueError('Unknown shape')
class Observer:
    def __init__(self, id):
        self.id = id
    def update(self, message):
        print(f"Received update: {message}")
class Subject:
    def __init__(self):
        self.observers = []
    def attach(self, obs):
        self.observers.append(obs)
    def detach(self, obs):
        self.observers.remove(obs)
    def notify(self, message):
        for o in list(self.observers):
            o.update(message)
if __name__ == '__main__':
    shape = shape_factory('circle')
    shape.draw()
    subject = Subject()
    obs1 = Observer(1)
    obs2 = Observer(2)
    subject.attach(obs1)
    subject.attach(obs2)
    subject.notify('update available!')
