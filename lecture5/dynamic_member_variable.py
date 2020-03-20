class Animal:
    pass

a = Animal()
b = Animal()
a.name = "Charles"
print(a.name)
# print(b.name)
Animal.name = "Charles"
print(b.name)
c = Animal()
print(c.name)

# def my_set_name(self, name):
#     self.name = name

# Animal.set_name = my_set_name
# a.set_name("Alice")
# print(a.name)
