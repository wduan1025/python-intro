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
    # YOUR CODE HERE
    # get the integer part of this number
    # YOUR CODE HERE
    # get the decimal part of the number and replace the number with it
    # YOUR CODE HERE
    # we have got one more digit, so increment the counter
    # YOUR CODE HERE
    # if the counter reaches maximum number of digits, terminate the loop
    # YOUR CODE HERE

print('binary representation for {decimal} is {binary}'.format(decimal=num, binary=digits))