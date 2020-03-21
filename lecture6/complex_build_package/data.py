class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def __str__(self):
        return "real is {r}, img is {i}".format(r=self.real, i=self.img)
        
    def __add__(self, another_complex):
        new_real = self.real + another_complex.img
        new_complex = self.img + another_complex.img
        return complex(new_real, new_complex)