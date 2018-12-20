n = int(input())
d = int(input())
arr = []
dic = {}

for i in range(n-1):
	rua = int(input())
	arr.append(rua)

arr = sorted(arr,reverse=True)
arr.append(d)
power2 = set()
for i in range(13):
	power2.add(2**i)
#print(arr)
for i in range(len(arr)):
	dic[i] = (1,arr[i])
	arr[i] = [i]
count = 0
## big change
#print(arr)
while len(arr) not in power2:
	a = arr[count][0]
	b = arr[count+1][0]
	a_v = dic[a][1]
	b_v = dic[b][1]
	dic[a] = ((a_v/(a_v+b_v)), a_v)
	dic[b] = (b_v/(a_v+b_v) ,b_v)
	arr = arr[:count] +[[a,b]] + arr[count+2:]  
	count+=1
#print(arr,dic)
while True:
	new_len = int(len(arr)/2)
	
	new_arr = [0] * new_len
	#print(new_len)
	for i in range(new_len):
		if i ==(new_len-1):
			first = arr[i*2]
			d = arr[i*2+1]
			for s in d:
				total_p = 0
				ps = dic[s][0]
				s_v = dic[s][1]
				for f in first:
					pf = dic[f][0]
					f_v = dic[f][1]
					#print(pf,ps,s_v,f_v)
					total_p += pf * ps * s_v/(f_v+s_v)
				dic[s] = (total_p, s_v)
			new_arr[i] =d
		else:
			#print(i)
			first = arr[i*2]
			second = arr[i*2+1]
			third = first + second
			memory = [0] * len(first) 
			
			for f in range(len(first)):
				total_p = 0
				pf = dic[first[f]][0]
				f_v = dic[first[f]][1]
				for s in second:
					ps = dic[s][0]
					s_v = dic[s][1]
					total_p += pf * ps * f_v/(f_v+s_v)
				memory[f] = total_p
			for s in second:
				total_p = 0
				ps = dic[s][0]
				s_v = dic[s][1]
				for f in first:
					pf = dic[f][0]
					f_v = dic[f][1]
					total_p += pf * ps * s_v/(f_v+s_v)
				dic[s] = (total_p,s_v)
			for j in range(len(first)):
				dic[first[j]] = (memory[j], dic[first[j]][1])
			
			new_arr[i] = third

	#print(dic)
	arr= new_arr
	if len(arr)==1:
		break
print(dic[n-1][0])



