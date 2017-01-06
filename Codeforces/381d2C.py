cases = input().split()
n= int(cases[0])
m = int(cases[1])
least_mex = 1000000
'''
dic = {}
for ele in range(n):
	dic[ele] = []

collection = []
starts = []
ends  = []
'''
for i in range(m):
	inputs = input().split()
	start = int(inputs[0])
	#starts.append(start)
	end = int(inputs[1])
	#ends.append(end)

	value = end-start + 1
	#collection.append([x for x in range(value)])
	#for g in range(start-1, end):
		#dic[g].append(i)
	if value <least_mex:
		least_mex = value
print(least_mex)
for j in range(n):
	print(str(j%least_mex), end=' ')
'''
@@@@  second try, turns to be really really dump
@@@@  attmpted to have a comprehensive way to sovle the whole thing.

def find_max(dic):
	# return the key of the maxium
	maxium = 0
	for i in dic:
		if len(dic[i])>len(dic[maxium]):
			maxium = i
	return maxium
def is_next_state(current_case):
	for i in range(len(collection)):
		a = collection[i]
		if current_case in a:
			return False
	return True
def is_all_case(all_cases, current_case):
	for i in all_cases:
		if current_case not in collection[i]:
			return False
	return True
def del_from_collec(all_cases, current_case):
	for i in all_cases:
		if current_case in collection[i]:
			collection[i].remove(current_case)
def is_all_case2(all_cases, current_case):
	for i in all_cases:
		if current_case in collection[i]:
			return False
	return True
def is_full(arrya):
	for h in array:
		if h == -1:
			return False
	return True
array = [-1]*n
current_case = 0
#print(dic)
for j in range(n):
	next_state = False
	comb_dict = {}
	counter = 0
	mirror_dic = {}
	for g in dic:
		mirror_dic[g] = dic[g]
	#print('0000000000000000000000000000000')
	full = is_full(array)
	if full:
		pass
	else:
		while not next_state:
			counter += 1
			next_state = is_next_state(current_case)
			if next_state:
				current_case += 1
			else:
				key = find_max(mirror_dic)
				if array[key] != -1:
					pass
				else:
					#print('-----------')
					#print(mirror_dic)
					#print(key, array, collection, current_case,comb_dict, n)
					all_cases = mirror_dic[key]
					if is_all_case(all_cases, current_case):
						array[key] = current_case
						del_from_collec(all_cases, current_case)
						full = is_full(array)
						if full:
							next_state = True
					else:
						if is_all_case2(all_cases, current_case):
							pass
						else:
							comb_dict[key] = mirror_dic[key]
						if counter == n:
							for z in comb_dict:
								if not is_all_case2(comb_dict[z], current_case):
									array[z] = current_case
									del_from_collec(comb_dict[z], current_case)
							full = is_full(array)
							if full:
								next_state = True
				if key in mirror_dic:
					del mirror_dic[key]
end = str(array[0])
for i in range(1, len(array)):
	end = end + ' ' + str(array[i])
print(least_mex)
print(end)
'''

'''
array = [0] * n
array1 = [0] * n
for j in range(least_end-least_start+1):
	array[least_end - 1 +j] = j

for z in range(len(starts)):
	start = starts[z]
	end = ends[z]
	if array1[start-1] == 0 and array1[end-1] ==0:
		for q in range(end-start+1):
			array1[start-1+q] = 1
			array[start-1+q] = q
	elif array1 
'''