f = open("friends_small", "r")
print(f)
content = f.read()
content_read_again = f.read()
print(content_read_again)
f.close()