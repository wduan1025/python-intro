class Life:
    def __init__(self, quality, lifetime):
        self._quality = quality
        self._lifetime = lifetime
    
    def get_quality(self):
        return self._quality
    
    def get_lifetime(self):
        return self._lifetime

    def __len__(self):
        return self._lifetime
    
    def __add__(self, another_life):
        combined_quality = (self._quality + another_life.get_quality()) / 2
        combined_lifetime = self._lifetime + another_life.get_lifetime()
        result = Life(combined_quality, combined_lifetime)
        return result

life1 = Life(1.2, 75)
print(life1.xxx)
life2 = Life(2, 60)
combined = life1 + life2
print("Combined life quality is ", combined.get_quality())
print("Combined life lifetime is ", combined.get_lifetime()) 
