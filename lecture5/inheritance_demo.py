class animal:
    def __init__(self, name):
        print("__init__ of animal")
        self.name = name
    
    def make_sound(self):
        print("hahahaha")

class cat(animal):
    pass

cat1 = cat("Andrew")
print(cat1.make_sound())


