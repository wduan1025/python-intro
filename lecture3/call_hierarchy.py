
def get_square_sum(l):
    return sum(get_square(l))

def get_square(l):
    return [i**2 for i in l]

print(get_square_sum([1,2,3]))