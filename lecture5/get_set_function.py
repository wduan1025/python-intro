class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("WoofWoof")

    def __len__(self):
        return len(self.name)

def small_bark():
    print("woooo")

dog = Dog("Alex")

dog.bark()
dog.__setattr__("bark", small_bark)
dog.bark()