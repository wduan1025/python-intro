a = [1,2,3]
try:
    item = a[4]
except:
    print("Index limit exceeded")
    item = None
print(item)