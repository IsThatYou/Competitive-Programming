import random
a = open("knockout_Tournament.in","w")
num = 2049
a.write("{}\n".format(num))
for i in range(num):
	a.write("{}".format(random.randint(1,10e5)))
	a.write("\n")
a.close()