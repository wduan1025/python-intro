<<<<<<< HEAD
class Myset():
    a = {1,2,3,4,5,6,7}
    def add(self,l):
        result = self.a.union(l)
        print(result)
    def remove(self,element):
        result2 = self.a.remove(element)
        print(result2)
    def _sub_(self,l):
        result = self.a - l
=======
# class Myset():
#     a = {1,2,3,4,5,6,7}
#     def add(self,l):
#         result = self.a.union(l)
#         print(result)
#     def remove(self,element):
#         result2 = self.a.remove(element)
#         print(result2)
#     def _sub_(self,l):
#         result = self.a.difference(l)
#         return result

# l = {6,7,8,9,10}
# element = 7
# Myset().add(l)
# Myset().remove(element)
# print(Myset().a-l)

class MySet:
    def __init__(self):
        self.items = []
    
    def add(self, num):
        if num in self.items:
            return
        self.items.append(num)
    
    def remove(self, num):
        self.items.remove(num)
    
    def __sub__(self, another_set):
        items1 = self.items
        items2 = another_set.items
        diff = [i for i in items1 if not i in items2]
        result = MySet()
        for i in diff:
            result.add(i)
>>>>>>> cbf96f5fdb6afd59661fa59d3b801c301de673ab
        return result
    
    def __str__(self):
        return '{' + ','.join([str(i) for i in self.items]) + '}'

s = MySet()
s.add(1)
s.add(2)
s.add(1)

<<<<<<< HEAD
l = {6,7,8,9,10}
element = 7
Myset().add(l)
Myset().remove(element)
print(Myset().a - l)
=======
t = MySet()
t.add(2)
t.add(3)
print(s-t)
>>>>>>> cbf96f5fdb6afd59661fa59d3b801c301de673ab
