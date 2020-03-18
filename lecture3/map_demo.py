l = [1,2,3,4]

l_map1 = map(lambda x: x+2, l)
print(list(l_map1))

def power_exp(x):
    sum_of_exponential = 0
    n = 4
    for i in range(n):
        sum_of_exponential += x**i
    return sum_of_exponential

l_map2 = map(power_exp, l)
print(list(l_map2))