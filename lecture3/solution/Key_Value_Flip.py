a = {"Alice":1 , "Simon":2 , "Boson":3 , "John":4}

# for c,d in a.items():
# 	c,d = d,c
# 	print (c,d)

print({v:k for k,v in a.items()})