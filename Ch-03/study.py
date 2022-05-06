from pyrsistent import b


class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal = Cal(2, 3)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
