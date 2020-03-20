class Dog:
    '''
    This is the class for Dog
    '''
    def __init__(self):
        self.name = "Doug"
    def bark(self):
        print("WoofWoof")

dog = Dog()
print(dog.__doc__)