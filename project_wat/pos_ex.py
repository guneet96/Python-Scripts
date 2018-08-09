f = open("new.txt", "r")
lines = f.readlines()
f.close()
temp = []
posl = []
for i in lines:
	temp = i.split()
	temp.pop(0)
	posl.append(temp[0])

#print posl		
