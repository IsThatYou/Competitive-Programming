cases = input().split()
x1 = int(cases[0])
y1 = int(cases[1])
cases = input().split()
x2 = int(cases[0])
y2 = int(cases[1])
cases = input().split()
x3 = int(cases[0])
y3 = int(cases[1])

answer = set()
v1 = (x1-x2, y1-y2)
v2 = (x1-x3, y1-y3)
v3 = (x2 -x3, y2-y3)
v4 = (x2-x1, y2-y1)
a1 = (v1[0] + x3, v1[1]+y3)
a2 = (v2[0] + x2, v2[1]+y2)
a3 = (v3[0] + x1, v3[1]+y1)
a4 = (v4[0] + x3, v4[1]+y3)
answer.add(a1)
answer.add(a2)
answer.add(a3)
answer.add(a4)
print(3)
for i in range(len(answer)):
	res = answer.pop()
	print("{} {}".format(res[0], res[1]))