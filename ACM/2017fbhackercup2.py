a = open("lazy_loading.txt")
b = open("output.txt", "w", newline = "\n")
along = int(a.readline())
for i in range(along):
	cases = int(a.readline())
	result = 0
	rest = cases
	ground = []
	for j in range(cases):
		item = int(a.readline())
		if item >= 50:
			result += 1
			rest -= 1
		else:
			phi = 50 / item
			phi_c = int(50/item)
			if phi == phi_c:
				phi -= 1
			else:
				phi = phi_c
			ground.append((item, phi))
	ground.sort(key=lambda x: x[1])
	print(ground)
	for j in range(len(ground)):
		need = ground[j][1]
		if rest > need:
			result += 1
			rest -= need+1
	print("Case #{}: {}".format(i+1, result), file=b)