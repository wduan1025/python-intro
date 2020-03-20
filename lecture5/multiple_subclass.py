class animal:
    def __init__(self, name):
        print("Creating object")
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def make_sound(self):
        print("hahahaha")

class cat(animal):
    def make_sound(self):
        print("Mew")

class dog(animal):
    def make_sound(self):
        print("Woof")

cat1 = cat("Andrew")
print(cat1.make_sound())
print(cat1.get_name())

dog1 = dog("Doug")
print(dog1.make_sound())
print(dog1.get_name())


