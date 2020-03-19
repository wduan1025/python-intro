
l = [1,2,3]
def append_x():
    l.append("x")

def append_y():
     l.append("y")
     l = []

def append_z():
    l = []
    l.append("z")

append_y()
print(l)
