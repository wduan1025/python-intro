names = ["Adam", "Barack", "Carol", "Nancy", "Zeb"]
target = "Nancy"
for name in names:
    if name == target:
        print("{target} found".format(target=target))
        break