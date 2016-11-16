vals = input().split()
n = int(vals[0])
k = int(vals[1])
if k > n:
    k = n

payments = [0]*n
deductions = [0]*n
for i in range(n):
    vals = input().split()
    payments[i] = int(vals[0])
    deductions[i] = int(vals[1])


all = []
for i in range(n):
	all.append(payments[i] + deductions[i])

all.sort(reverse = True)
sums = 0
ded = 0
earnings = -1 * sum(deductions)
for i in range(k):
	earnings += all[i]


if earnings > 0:
	print(earnings)
else:
	print(0)