def increment(l):
    return [i+1 for i in l]

def decrement(l):
    return [i-1 for i in l]

another_decrement = decrement

def process_list(l, f):
    return f(l)

l = [1,2,3]
print(process_list(l, increment))
print(process_list(l, decrement))
print(process_list(l, another_decrement))