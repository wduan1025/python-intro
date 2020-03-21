class Dog():
    owner = None

    def set_owner(self, new_owner):
        self.owner = new_owner
    
    def get_owner(self):
        return self.owner

class Human():
    name = None
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

dog = Dog()
sophie = Human()
sophie.set_name("Sophie")
print("Dog initial owner is ", dog.get_owner())
dog.set_owner(sophie)
print("Dog owner is ", dog.get_owner().get_name())

dog.get_owner().set_name("Trevor")
print("Now sophie's name is ", sophie.get_name())