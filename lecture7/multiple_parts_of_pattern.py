import re
scientists = "Issac Newton, Albert Einstein, Erwin Schrodinger, Werner Heisenberg"
pattern = r"(\w+) (\w+)"
print(re.findall(pattern, scientists))