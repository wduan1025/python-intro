class iterable(list):
    def __int__(self):
        self.items = []
    def append(self, a):
        if a in self.items:
            return
        self.items.append(a)
    def len(self):
        l = len(self.items)
        return l
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        try:
            result = self.items(self.index)
            self.index += 1
        except IndexError:
            raise StopIteration
        return result