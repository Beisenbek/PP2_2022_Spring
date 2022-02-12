class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printMe(self):
        print(self.name + " " + str(self.age))


p1 = Person("John", 36)
p1.printMe()

p2 = Person("Boris", 20)
p2.printMe()