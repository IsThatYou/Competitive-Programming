# https://www.hackerrank.com/contests/university-codesprint-2/challenges/game-of-two-stacks
g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    sums = 0
    counter = 0
    for i in range(n):
    	counter += 1
    	sums += a[i]
    	if sums > x:
    		counter -= 1
    		sums -=a[i]
    		break
    if sums > x:
    	counter -= 1
    	sums -=a[i]

    longest = counter
    archor = 0
    for i in range(counter, -1, -1):
    	for j in range(archor, m):
    		counter += 1
    		sums += b[j]
    		if sums  > x:
    			sums -= b[j]
    			counter -=1
    			archor = j
    			break
    	archor = j
    	if sums >x:
    		sums -= b[j]
    		counter -=1


    	if counter > longest:
    		longest = counter
    	counter -= 1
    	lost = a[i-1]
    	sums -= lost

    print(longest)
