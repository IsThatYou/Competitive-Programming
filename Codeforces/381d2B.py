cases = input().split()
n = int(cases[0])
m = int(cases[1])
array = input().split()
sums = 0
for i in range(m):
	inputs = input().split()
	start = int(inputs[0])
	end = int(inputs[1])
	sub = array[start-1:end]
	value = 0
	for j in sub:
		value += int(j)
	if value >= 0:
		sums += value
print(sums)