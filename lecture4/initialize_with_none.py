some_name = "Peter"
class Cat():
    name = None
    age = 2
    owner = some_name

cat = Cat()
print(cat.name)
print(cat.name is None)
cat.name = "Adam"
print(cat.name)