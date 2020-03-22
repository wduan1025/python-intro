def fibonacci(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

m = fibonacci(8)

if __name__ == "__main__":
    n = 10
    print(__name__)
    print(fibonacci(n))