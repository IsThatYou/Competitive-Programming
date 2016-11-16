val = input().split()
row = int(val[0])
col = int(val[1])
k = int(val[2])

record = []
for i in range(k):
	record.append([])

for j in range(k):
	val = input().split()
	nrow = int(val[0])
	start = int(val[1])
	end = int(val[2])
	hm = True
	for i in range(j):
		if record[i] != []:
			nrow2 = record[i][0]
			first = record[i][1]
			last = record[i][2]
			if nrow == nrow2:
				if start >= first:
					if start > last:
						pass
					elif start <= last:
						hm = False
						if end >= last:
							record[i][2] = end
							
				elif start < first:
					if end < first:
						pass
					elif end >= first:
						record[i][1] = start
						hm = False
						if end > last:
							record[i][2] = end
	if hm:
		record[j] = [nrow, start, end]
print(record)

			



sums = 0
for i in range(len(record)):
	if record[i] != []:
		ssum = record[i][2] - record[i][1] + 1
		sums += ssum
result = row * col - sums

print(result)




