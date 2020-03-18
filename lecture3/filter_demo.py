l = [1,2,3,4,5,6,7]

l_filter1 = filter(lambda x: x>2, l)
print(list(l_filter1))

def power_exp(x):
    sum_from_zero = 0
    for i in range(x):
        sum_from_zero += i
    return sum_from_zero > 20

l_filter2 = filter(power_exp, l)
print(list(l_filter2))