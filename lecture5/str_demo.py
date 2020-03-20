class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
    
    def __str__(self):
        return "Dog name: {dog_name} Owner name: {owner_name}".format(dog_name=self.name, owner_name=self.owner.name)
class Human:
    def __init__(self, name):
        self.name = name

some_owner = Human("Charlie")
some_pet = Dog("Adam", some_owner)
print(some_pet)