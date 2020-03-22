class MyList(list):
    def __getitem__(self, i):
        return super().__getitem__(i-1)

    def __sub__(self, another_mylist):
        return [i for i in self if not i in another_mylist]

a = MyList([1,2,3])
b = MyList([1,4,5])
print(a)
# print(a-b)
print(b[3])
