class animal:
    def __init__(self, name):
        self.name = name
class pet(animal):
    def __init__(self, name, owner_name):
        super().__init__(name)
        self.owner_name = owner_name
class wild(animal):
    def __init__(self, name, num_caves):
        super().__init__(name)
        self.num_caves = num_caves

class flyable(animal):
    def fly(self):
        print(self.name, "is flying")
class runnable(animal):
    def run(self):
        print(self.name, "is running")

class Parrot(pet, flyable):
    pass
class Dog(pet, runnable):
    pass
class Bat(wild, flyable):
    pass
class Rat(wild, runnable):
    pass

parrot = Parrot("Alice", "Bob")
dog = Dog("Carol", "Dave")
bat = Bat("Bruce", 2)
rat = Rat("Henry", 3)

dog.run()
bat.fly()