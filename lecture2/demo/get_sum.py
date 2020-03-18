l = [1,2,3,4,5,6,7]
current_sum=0
current_index=0
while current_sum < 20:
    print(current_sum, '  ', current_index)
    current_sum += l[current_index]
    current_index += 1

print(current_sum)
