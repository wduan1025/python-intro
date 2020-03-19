class Dog():
    def __init__(self, name, age):
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

dog1.introduce()
dog2.introduce()
