import re
s = "I'm a software_engineer with 4.5 yrs exp,\nI have 12   projects on www.github.com"
print(s)
pattern = r"[123]"
# pattern = r"[1-9]"
# pattern = r"[^1-9]"
# pattern = r"[a-z]"
pattern = r"[a-zA-Z]"
pattern = r"[ab1c2]"
# pattern = r"[a-zA-Z_]"
print(re.findall(pattern, s))