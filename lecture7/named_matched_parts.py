import re
name = "Donald John Trump"
pattern = r"(?P<firstname>\w+) (?P<middlename>\w+) (?P<lastname>\w+)"
m = re.match(pattern, name)
print(m.group("firstname"))
print(m.group("lastname"))