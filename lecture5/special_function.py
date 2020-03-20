class Dog:
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        return len(self.name)

dog = Dog("Bob")
print(dog.__dir__())