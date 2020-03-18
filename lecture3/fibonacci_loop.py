num1 = 1
num2 = 1
n = 3
for i in range(n-2):
    prev_num2 = num2
    num2 += num1
    num1 = prev_num2

print("The NO.{n} number in fibonacci series is {num2}".format(n=n, num2=num2))