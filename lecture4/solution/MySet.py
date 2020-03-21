class Myset():
    a = {1,2,3,4,5,6,7}
    def add(self,l):
        result = self.a.union(l)
        print(result)
    def remove(self,element):
        result2 = self.a.remove(element)
        print(result2)
    def _sub_(self,l):
        result = self.a.difference(l)
        return result

l = {6,7,8,9,10}
element = 7
Myset().add(l)
Myset().remove(element)
print(Myset().a-l)