import dis

sum_of_numbers = 0
def example(x):
     for i in range(x):
         sum_of_numbers += i
         print(x)

print(dis.dis(example))