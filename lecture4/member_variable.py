some_name = "Peter"
class Cat():
    name = "Charles"
    age = 2
    owner = some_name

cat = Cat()
print(cat.name)
cat.name = "James"
print(cat.name)
print("Owner of the cat is ", cat.owner)