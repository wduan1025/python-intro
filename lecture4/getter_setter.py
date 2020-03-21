class Dog():
    name = "Bukky"
    age = 3

    def bark(self):
        print("WoofWoof")
        
    def set_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

dog = Dog()
print("Dog initial name is ", dog.get_name())
dog.set_name("Charlie")
print("New name of dog is ", dog.get_name())