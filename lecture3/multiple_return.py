def get_min_and_max_from_list(l):
    min_val = min(l)
    max_val = max(l)
    return min_val, max_val

l = [1,6,4,6,-8,3,0,14,7,9]
result = get_min_and_max_from_list(l)
print("result is ", result)
print("type of result is", type(result))

a, b = get_min_and_max_from_list(l)
print("min value is ", a)
print("max value is ", b)