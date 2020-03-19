class Circle:
    __pi = 3.14159
    radius = 0
    def set_radius(self, r):
        self.radius = r
    def get_area(self):
        return self.__pi * self.radius**2

circle = Circle()
radius=5
circle.set_radius(5)
print("Area of a radius={r} circle is {s}".format(r=radius, s=circle.get_area()))
print(circle._Circle__pi)