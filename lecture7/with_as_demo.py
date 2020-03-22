with open("friends_small", "r") as f:
    lines = f.readlines()
    print("Read {n} lines".format(n=len(lines)))

print("Lines of file is ", lines)