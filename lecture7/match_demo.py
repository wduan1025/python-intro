import re

s = "I'm John,I'm a software_engineer with 4.5 yrs exp,\nI have 112   projects on www.github.com"
pattern = r"I'm"
m = re.match(pattern, s)
print(m)