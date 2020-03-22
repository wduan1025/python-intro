import re
with open("urls", "r") as f:
    content = f.read()
    pattern = r"www.([\w\d]+).com"
    company_names = re.findall(pattern, content)

print(company_names)