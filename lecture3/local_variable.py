a = 1
b = 2

def add(a=3, b=4):
    print("In function", a, b)
    s = a+b
    return s

t = add(a, b)
print(t)
print(a)
print(b)