f = open("neg_words.txt", "r")
lines = f.readlines()
f.close()
temp = []
negl = []
for i in lines:
        temp = i.split()
        negl.append(temp[0])

#print negl
	
