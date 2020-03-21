class Dog():
    name = "Bukky"
    age = 3

    def bark(self):
        print("WoofWoof")
        
    def set_name(self, new_name):
        self.name = new_name

dog = Dog()
print("Dog's name is ", dog.name)
dog.name = "Charles"
print("Dog's new name is ", dog.name)
dog.set_name("Adam")
print("Dog's latest name is ", dog.name)