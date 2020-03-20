def fibonacci(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return fibonacci(n-1)*fibonacci(n-2)*fibonacci(n-3)

print(fibonacci(4))