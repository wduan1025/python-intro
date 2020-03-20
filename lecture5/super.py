class animal:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("my name is ", self.name)

class cat(animal):
    def introduce(self):
        print("Mew!")
        super().introduce()

cat1 = cat("Andrew")
cat1.introduce()