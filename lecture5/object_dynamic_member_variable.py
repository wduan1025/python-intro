class Dog:
    __slots__ = ("name", "bark")

dog = Dog()
dog.name = "Charles"
print(dog.name)
# dog.age = 2
# print(dog.age)

def my_bark(self):
    print(self.name, "is barking")

def my_introduce(xx):
    print("Hi I'm", xx.name)

Dog.intro = my_introduce
dog.intro()