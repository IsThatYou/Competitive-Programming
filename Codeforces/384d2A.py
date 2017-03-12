cases = input().split()
n = int(cases[0])
a = int(cases[1])
b = int(cases[2])
string = input()
a_type = 0
b_type = 0
find_b = False
more = False
b_index=0
a_index=0
for i in range(len(string)):
	if i + 1 == a:
		a_type = string[i]
		a_index = i
	if i + 1 == b:
		b_type = string[i]
		b_index = i
		find_b = True
if a_type == b_type:
	print(0)
else:
	print(1)
	'''
	counter = 1
	minium = 100005
	weitght = True
	while True:
		if a_index+counter < len(string):
			if string[a_index+counter] != a_type:
				num = abs(counter)
				if num < minium:
					minium = num
				break
		if a_index-counter > 0:
			if string[a_index-counter] != a_type:
				num = abs(counter)
				if num < minium:
					minium = num
				break
		if a_index+counter > len(string) and a_index-counter < 0:
			break
		counter+=1
	counter = 1
	while True:
		if b_index+counter < len(string):
			if string[b_index+counter] != b_type:
				num = abs(counter)
				if num < minium:
					minium = num
				break
		if b_index-counter > 0:
			if string[b_index-counter] != b_type:
				num = abs(counter)
				if num < minium:
					minium = num
				break
		if b_index+counter > len(string) and b_index-counter < 0:
			break
		counter += 1
	print(minium)
	'''

 