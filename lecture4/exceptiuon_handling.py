l = [1,2,3,4]
target = 0
print("target is ", target)
def find_index(l, target):
    try:
        value = l[target]
        print("value is ", value)
    except:
        print("there's an exception")
        value = -1
    return value

print(find_index(l, target))