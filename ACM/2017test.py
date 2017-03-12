
a = open("fightingthezombie.out")
b = open("output.txt")

print(a.readlines)
for i in a.readlines():
	comp = b.readline()
	if i!= comp:
		print(comp)
		print(i)

a.close()
b.close()