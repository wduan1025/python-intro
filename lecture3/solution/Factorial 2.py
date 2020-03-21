def factorial(n):
    if n > 0:
        a = 1
        for i in range (1,n+1):
            a *= i
        return (a)
    else:
        print("Error: Negative Number")
        return None


c = factorial (4)
print(c)