
def greedy_helper(coins,m):
	num = 0
	for coin in coins:
		if coin > m:
			pass
		else:
			num+=m//coin
			m = m%coin
	return num
	
	
n = int(input())
coins = list(map(int,input().split()))
flipped_coins = coins[::-1]


m = [0 for a in range(2*coins[-1])]
for i in range(1,2*coins[-1]):
	possible_ways = set()
	for coin in coins:
		if i-coin >=0:
			possible_ways.add(m[i-coin])
		else:
			break
	m[i] = min(possible_ways)+1
	#print(m[i],greedy_helper(flipped_coins,i))
	if not m[i] == greedy_helper(flipped_coins,i):
		print("non-canonical")
		break
else:
	print("canonical")
