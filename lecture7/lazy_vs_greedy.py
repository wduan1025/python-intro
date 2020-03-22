import re

s = "I'm a software_engineer with 4.5 yrs exp,\nI have 112   projects on www.github.com"
pattern = r"[1-9.]+"
pattern = r"[1-9.]+?"
pattern = r"[1-9.]{2,3}?"
print(re.findall(pattern, s))