class Life:
    def __init__(self, quality, lifetime):
        self._quality = quality
        self._lifetime = lifetime
    
    def __len__(self):
        return self._lifetime

life = Life(1.2, 75)
print("My life span is ", len(life))