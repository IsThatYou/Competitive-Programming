n = int(input())
s = input().strip().split()
dic = {}
aset = set()
for i in range(n):
	dutch = s[i]
	if dutch in dic:
		dic[dutch][0] += 1
	else:
		dic[dutch] = [1,0,0,""]
	aset.add(dutch)
m = int(input())

for i in range(m):
	dutch,english,right = input().split()
	
	if dutch in dic:
		dic[dutch][3] = english
		if right == "correct":
			dic[dutch][1] += 1
		else:
			dic[dutch][2] += 1
	else:
		dic[dutch] = [1,0,0,english]
		if right == "correct":
			dic[dutch][1] += 1
		else:
			dic[dutch][2] += 1


#print(dic)
ans = [1,0]
for i in aset:
	#print(i)
	num_right = dic[i][1] **(dic[i][0])
	num_wrong = (dic[i][2]+dic[i][1]) **(dic[i][0]) - num_right
	num_total = num_right + num_wrong
	
	if ans[1] == 0:
		ans[1] = ans[0] * num_wrong
	else:
		ans[1] = ans[1] * num_total + ans[0] * num_wrong
	ans[0] = ans[0] * num_right
if sum(ans) == 1:
	string = dic[s[0]][3]
	for i in range(1,n):
		string = string + " " + dic[s[i]][3]
	print(string)
	if ans[0] == 1:
		print("correct")
	else:
		print("incorrect")
else:
	print(ans[0],"correct")
	print(ans[1],"incorrect")




