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

    def make_sound(self, name):
        print(name)
        self.mew()

c = cat()
c.make_sound("xx")
