length = input().strip()
s = input().strip()

def screen(a, b, target):
	new = []
	for i in target:
		if i == a or i == b: 
			new.append(i)
	return new

def checkalternate(a, b, target):
	counter = 0
	last = ''
	while True:
		if target[counter] ==  a:
			if last == a:
				break
			last = a
		elif target[counter] == b:
			if last == b:
				break
			last = b
		counter += 1
		if (counter) == len(target):
			return True


	return False

b = set()
for i in s:
	b.add(i)
distinct = len(b)

c = []
for x in b:
	c.append(x)

maxlength = 0

for i in range(len(b)):
	out = b.pop()
	for j in b:
		out2 = j
		new = screen(out, out2, s)
		result = checkalternate(out, out2, new)
		if result == True:
			newlength = len(new)
			if maxlength < newlength:
				maxlength = newlength

print(maxlength)




