# https://www.hackerrank.com/contests/university-codesprint-2/challenges/breaking-best-and-worst-records
n = int(input())
s = input().split()
highest = int(s[0])
hcount = 0
least = int(s[0])
lcount = 0
s= s[1:]
for i in s:
	if int(i) >highest:
		highest = int(i)
		hcount += 1
	elif int(i) < least:
		least = int(i)
		lcount += 1
print(str(hcount), str(lcount), sep = " ")