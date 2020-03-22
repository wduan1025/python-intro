import re

s = s = "I'm a software_engineer with 4.5 yrs exp,\nI have 112   projects on www.github.com"
pattern = r"www[\w.]+.com"
pattern = r"www([\w.]+).com"
print(re.findall(pattern, s))