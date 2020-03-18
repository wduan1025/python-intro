def fibonacci(k):
    if k <= 2:
        return 1
    else:
        return fibonacci(k-1) + fibonacci(k-2)

print(fibonacci(6))