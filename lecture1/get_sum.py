# Usage:
# python get_sum.py <num1> <num2>
# Example:
# python get_sum.py 2 3
# expected output: 5

# problem3: run this program with different arguments and see how it works
# problem4: read the codes in this file, modify some parts, try to enable three
# arguments and get the sum of them
import argparse

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser(description='Print the sum of numbers.')
parser.add_argument("num1", help="First number", type=int)
parser.add_argument("num2", help="Second number", type=int)

args = parser.parse_args()
print( args.num1 + args.num2)