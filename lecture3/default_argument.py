def increment_list(l=[0, 0]):
    l.append(l[-2] + l[-1])
    return l

print(increment_list([2,3]))
print(increment_list())
print(increment_list())