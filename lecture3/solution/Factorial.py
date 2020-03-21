def factorial(n):
    if n > 0:
        if n == 0 or n == 1:
            return 1
        else:
            a = n * factorial (n-1)
        return a
    else:
        print("Error: Negative Number")
        return None

# ideas:
# n == 0 or n == 1
# for i in range (1,n+1)
# a = 1 * i

a = factorial (4)
print(a)