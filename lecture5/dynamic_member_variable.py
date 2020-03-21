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
