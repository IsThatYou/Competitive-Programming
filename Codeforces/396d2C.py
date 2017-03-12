n = int(input())
s = input()
cons = [int(x) for x in input().split()]


def f(current):
 	a = current[0]
 	limit = cons[ord(a) - 97]
 	if len(current) == 1:
 		return 1
 	else:
 		sums = 0
	 	if limit < len(current):
	 		for i in range(1, limit+1):
	 			go = True
	 			for j in range(0, i):
	 				if cons[ord(current[j]) - 97] < i:
	 					go = False
	 					break
	 			if go:
	 				sums += f(current[i:])
	 	else:
	 		for i in range(1, len(current)):
	 			go = True
	 			for j in range(1,i):
	 				if cons[ord(current[j]) - 97] < i:
	 					go = False
	 			if go:
	 				print('ha', current)

	 				sums += f(current[i:])
	 		go2 = True
	 		for z in current:
	 			if cons[ord(z)-97] < len(current):
	 				go2 = False
	 				break
	 		if go2:
	 			sums += 1
	 	return sums
result = f(s)
print(result)