class Dogs:
    def __init__(self):
        self.dogs = []
    def __getitem__(self, i):
        if i*2 < len(self.dogs):
            return self.dogs[i*2]
        else:
            return None

dogs = Dogs()
dogs.dogs = ["Alice", "Bob", "Carol", "Dave", "James", "Mark", "Bruce"]
print(dogs[0])
print(dogs[2])
print(dogs[3])
print(dogs[4])