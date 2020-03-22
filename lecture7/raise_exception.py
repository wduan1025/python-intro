class MySet:
    def __init__(self):
        self.data = []
    
    def add(self, n):
        self.data.append(n)
    def __getitem__(self, idx):
        if idx >= len(self.data) or idx < -len(self.data):
            raise IndexError("Index Exceeded")
        return self.data[idx]

set = MySet()
set.add(2)
set.add(3)
print(set[0])
print(set[1])
print(set[2])