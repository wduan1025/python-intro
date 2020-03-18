income = 280000
tax_message = "Highest rate for ${income} is {rate}"
rate=0
if income < 14100:
    rate = 0.1
    rate*=2
    rate/=2
elif income < 53700:
    rate = 0.12
elif income < 85500:
    rate = 0.22
elif income < 163300:
    rate = 0.24
elif income < 207350:
    rate = 0.32
elif income < 518400:
    rate = 0.35
else:
    rate = 0.37
print(tax_message.format(income=income, rate=rate))
