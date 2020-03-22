import re
s = "The guy's phone number is 244234213"
pattern = r"(\d+)"
m = re.search(pattern, s)
print(m.span())