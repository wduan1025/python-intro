class Dog():
    name = "Charles"
    def __init__(self, name, age):
        print("In __init__ of Dog")
        self.name = name
        self.age = age

    def bark(self):
        print("WoofWoof")
        
    def set_name(self, new_name):
        self.name = new_name
    def introduce(self):
        print("Hi, my name is {name}, I'm {age} years old".format(name=self.name, age=self.age))

dog1 = Dog("Doge", 2)
dog2 = Dog("Adam", 3)
print(Dog.name)

dog1.introduce()
dog2.introduce()
