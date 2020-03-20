def fibonacci(k):
    print("Current k is ", k)
    if k <= 1:
        return 1
    else:
        return fibonacci(k-1) + fibonacci(k-2)

print(fibonacci(6))

# def xx():
#     return xx()
# a = xx()