class MyIterable(list):
    data = []
    def __int__(self):
        self.index = 0

    def add(self, a):
        if a in self.data:
            return
        self.data.append(a)

    def __len__(self):
        l = len(self.data)
        return l

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        try:
            result = self.data[self.index]
            self.index -= 1
        except IndexError:
            raise StopIteration
        return result

a = MyIterable()
print(a.data)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
for i in a:
    print(i)