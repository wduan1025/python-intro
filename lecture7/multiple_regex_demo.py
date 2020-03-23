import re

s = s = "I'm a software_engineer with 4.5 yrs exp,\nI have 1123   projects on www.github.com"
pattern = r"\d"
pattern = r"\d+"
pattern = r"\d*"
pattern = r"\d{3}"
# pattern = r"\d{1,3}"
# pattern = r"\d{1,3}"
pattern = r"[1-9.]+"
print(re.findall(pattern, s))