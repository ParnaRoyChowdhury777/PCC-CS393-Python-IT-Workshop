a = input("enter a string :")
l = a.split()
i =''
d = {"India":"West Bengal"}
l2=[]
for word in l:
	if word in d:
		l2.append(d[word])
	else:
		l2.append(word)
print(" ".join(l2))
