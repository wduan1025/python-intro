class Dog:
    __slots__ = ("name", "bark")

dog = Dog()
dog.name = "Charles"
print(dog.name)
def my_bark(self):
    print(self.name, "is barking")

# dog.age = 2
# print(dog.age)

def my_introduce(xx):
    print("Hi I'm", xx.name)

Dog.intro = my_introduce
dog.intro()