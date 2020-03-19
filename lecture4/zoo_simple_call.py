class Dog():
    name = "Bukky"
    age = 3

    def bark(self):
        print("WoofWoof")
        
class cat():
    name = "Seran"
    age = 2
    def mew(self):
        print("MewMew")

cat1 = cat()
mypet = cat()
mydog = Dog()

print("Cat1 is in ", cat1)
print("Cat2 is in ", mypet)

print("Name of cat1 is ", cat1.name)
print("Dog is barking:")
mydog.bark()