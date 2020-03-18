# Assume that num is between 0 and 1
# Get the binary representation of this number, up to 20 digits
# print the result  and compare with expected result

num = 0.1
# Initialize result
digits = '0.'
# Setup the maximum number of digits to calculate, use as stop condition
max_num_digits = 20
# Keep a counter of the number of digits we have got for now, initialize with 0
num_digits = 0
# make a temporary variable for calculation
decimal = num
while decimal > 0:
    # multiply the current number with 2
    decimal = decimal * 2
    # get the integer part of this number
    digit = int(decimal)
    # get the decimal part of the number and replace the number with it
    decimal = decimal - digit
    # convert the integer part to string, and append to teh result
    digits = digits + str(digit)
    # we have got one more digit, so increment the counter
    num_digits += 1
    # if the counter reaches maximum number of digits, terminate the loop
    if num_digits == max_num_digits:
        break

print('binary representation for {decimal} is {binary}'.format(decimal=num, binary=digits))