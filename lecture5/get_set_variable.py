class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("WoofWoof")

    def __len__(self):
        return len(self.name)

dog = Dog("Bob")
print(dog.__getattribute__("name"))
dog.__setattr__("name", "Carol")
print(dog.__getattribute__("name"))
