# Calculate the federal income tax according to the given tax bracket here
income = 280000
tax = 0
# YOUR CODE HERE
if income < 9525:
	tax = income * 0.1
elif income < 38700:
	tax = income * 0.12
elif income < 82500:
	tax = income * 0.22
elif income < 157500:
	tax = income * 0.24
elif income < 200000:
	tax = income * 0.32
elif income < 500000:
	tax = income * 0.35
else:
	tax = income * 0.37
print("total income tax you have to pay is {tax}".format(tax=tax))
