n = int(input())
array = input().split()

counter = 0
visited = []
while True:
	if counter not in visited:
		visited.append(counter)
	crush_index = array[counter]
	if crush_index in visited:
		pass
	counter = crush_index


