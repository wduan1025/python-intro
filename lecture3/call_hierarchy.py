
def get_square_sum(l):
    x = get_square(l)
    return sum(x)

def get_square(l):
    return [i**2 for i in l]

print(get_square_sum([1,2,3]))
