# https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot
def candy_replenishing_robot():
	n,t = input().strip().split(' ')
	n,t = [int(n),int(t)]
	c = list(map(int, input().strip().split(' ')))
	re = n
	count = 0
	for i in range(t-1):
		re -= c[i]
		if re < 5:
			count += n-re
			re = n
	print(count)
#candy_replenishing_robot()
def find_the_minimum_number():
	n = int(input())
	s = "min(int, " * (n-1) +  "int" + ")"*(n-1)
	print(s)
#find_the_minimum_number()
def melodious_password():
	n = int(input())
	vowel = ['a','e','i','o','u']
	cons = list(filter(lambda x: x not in vowel and x != 'y',[chr(i+97) for i in range(26)]))
	none = ['y']
	#print(cons)
	vowel_n = 5
	con_n = 20
	'''
	if n%2 == 0:
		answer = (vowel_n**(n/2) + con_n**(n/2))*2
	else:
		answer = vowel_n**(n/2+1) + con_n**(n/2) + vowel_n**(n/2) + con_n**(n/2+1)
	'''
	isvowel = True
	def help(v, last, count, maxx):
		if count == maxx:
			print(last)
		else:
			if v:
				for i in vowel:
					help(False, last+i, count+1, maxx)
			else:
				for i in cons:
					help(True, last+i, count+1, maxx)
	help(isvowel, "", 0, n)
	help(False, "", 0, n)

#melodious_password()
def poles():
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	hill = []
	for a0 in range(n):
	    x_i,w_i = input().strip().split(' ')
	    x_i,w_i = [int(x_i),int(w_i)]
	    hill.append((x_i, w_i, 0))
	last = 0
	hill[0]= (hill[0][0], hill[0][1], 1)
	total = 0
	for i in range(1,n):

		total += (hill[i][1])*(hill[i][0] - hill[0][0])

	for i in range(1, k):
		minimum = 0
		bench = 0
		for j in range(n):
			if hill[j][2] == 0:
				for z in range(0, j):
					if hill[z][2] == 1:
						last = z
				to = n
				for z in range(j+1, n):
					if hill[z][2] == 1:
						to = z 
						break
				diff = hill[j][0] - hill[last][0] 
				sums = 0
				for z in range(j, to):
					sums += hill[z][1] * diff
				if sums > minimum:
					minimum = sums
					bench = j
		hill[bench] = (hill[bench][0], hill[bench][1], 1)
		total -= minimum
	print(hill)
	print(total)




poles()