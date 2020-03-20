a = [1,2,3,4]
i = iter(a)
while True:
    try:
        k=next(i)
        print(k)
    except:
        break