class MyList:
    def __init__(self, capacity):
        self.max = capacity

    def __iter__(self):
        self.i = 0
        return self
        
    def __next__(self):
        if self.i < self.max:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration

l = MyList(10)
