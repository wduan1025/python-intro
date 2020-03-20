class Animal:
    def __init__(self, name):
        self.name = name

a = Animal("Charles")

def my_set_name(self, name):
    self.name = name
# def my_set_name(xx, name):
#     xx.name = name

Animal.set_name = my_set_name
a.set_name("Alice")
print(a.name)
