import re

s = "My name is John,I'm a software_engineer with 4.5 yrs exp,\nI have 112   projects on www.github.com"
pattern = r"I'm"
m = re.search(pattern, s)
print(m)