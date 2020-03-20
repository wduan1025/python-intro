some_name = "Peter"
class Cat():
    name = "Charles"
    age = 2
    owner = some_name

cat1 = Cat()
print(cat1.name)
cat1.name = "James"
print(cat1.name)

owner = "xxx"
print(owner)
print("Owner of the cat is ", cat1.owner)
