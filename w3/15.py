
class Building:
    class Room:
        def __init__(self, level):
            self.level = level
        def printMe(self):
            print("room at level " + str(self.level))

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.rooms = [self.Room(0),self.Room(1),self.Room(2),self.Room(3)]

    
    def printMe(self):
        for r in self.rooms:
            r.printMe()

    
'''
rm1 = Building("name", "number").Room(1)
rm1.printMe()
'''

#bd1 = Building("Esentai mall", "77")
#bd1.printMe()


