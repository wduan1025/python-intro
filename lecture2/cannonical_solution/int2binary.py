num = 23
temp_num = num
digits = ''
while temp_num > 0:
    digit = temp_num % 2
    digits = str(digit) + digits
    temp_num //= 2
print("binary for {num} is {digits}".format(num=num, digits=digits))