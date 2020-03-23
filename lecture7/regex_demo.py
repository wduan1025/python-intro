import re
s = "I'm a software_engineer with 4.5 yrs exp,\nI have 12   projects on www.github.com"
print(s)
# pattern = r'\d'
pattern = r"\D"
# pattern = r"\s"
pattern = r"\w"
# pattern = r"\W"
# cannot write r pattern
print(re.findall(pattern, s))