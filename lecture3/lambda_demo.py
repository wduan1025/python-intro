f = lambda x: x + [2]
print(f)
l = [1,2,3]
print(f(l))
print(l)

g = lambda x: x.append(2)
print(g(l))
print(l)

h = lambda *x: len(x)
print(h(1,2,3,4))

j = lambda **y: {k:v for k, v in y.items()}
print(j(name="Charles", age=22))
