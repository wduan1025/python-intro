class Cat():
    name = "Charles"
    age = 2
    owner = None

class Human():
    name = "Sophie"
    age = 15

cat = Cat()
print(cat.owner is None)
sophie = Human()
cat.owner = sophie
print(cat.owner)
print(cat.owner.name)