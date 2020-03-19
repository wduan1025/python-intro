x = [1,2,3]
def append_x(l):
    l.append('x')
    l[1] = 0
    
append_x(x)
print(x)
