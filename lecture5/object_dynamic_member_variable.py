class Dog:
    __slots__ = ("name", "bark")

dog1 = Dog()
dog1.name = "Charles"
print(dog1.name)
Dog.age = 3
# dog1.age = 2
# print(dog1.age)

def my_bark(self):
    print(self.name, "is barking")

def my_introduce(xx):
    print("Hi I'm", xx.name)

# Dog.bark = my_bark
# dog.bark()
Dog.intro = my_introduce
dog1.intro()