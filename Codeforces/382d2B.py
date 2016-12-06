cases = input().split()
n = int(cases[0])
n1 = int(cases[1])
n2 = int(cases[2])
array = input().split()
array = [int(x) for x in array]
array.sort()
less = min(n1, n2)
more = max(n1,n2)
sum1 = 0
sum2 = 0
for i in range(n-less, n):
	sum1 += array[i]

for j in range(n-less-more, n-less):
	sum2 += array[j]
result = sum1/less + sum2/more 
print(result)