#https://open.kattis.com/contests/mpf7xe/problems/connectthedots
import sys
def connect(s,e,matrix,dic):
	x1,y1 = dic[s]
	x2,y2 = dic[e]
	for i in range(min(x1,x2)+1,max(x1,x2)):
		if matrix[i][y1] == '.':
			matrix[i][y1] = '|'
		elif matrix[i][y1] == '-':
			matrix[i][y1] = '+'
	for i in range(min(y1,y2)+1,max(y1,y2)):
		if matrix[x1][i] == '.':
			matrix[x1][i] = '-'
		elif matrix[x1][i] == '|':
			matrix[x1][i] = '+'
	return matrix


x = 0
y = 0
matrix = []
dic = {}
for line in sys.stdin:
	y = 0
	new_l = list(line.strip())
	matrix.append(new_l)
	length = 0
	for char in range(len(new_l)):
		if new_l[char] != '.':
			dic[new_l[char]] = (x,y)
			length += 1
		y+= 1

	x += 1
	if line =="\n" : 
		x = 0
		y = 0
		c = 0
		nodes = list(dic.keys())
		#print(nodes)
		while c<len(nodes):
			start = nodes[c]
			if ord(start)< 65:
				if start == '9':
					end = 'a'
				else:
					end = chr(ord(start)+1)
			elif ord(start) < 97:
				if start == 'Z':
					end = -1
				else:
					end = chr(ord(start) + 1)
			else:
				if start == 'z':
					end = 'A'
				else:
					end = chr(ord(start) + 1)
			#print(start,end)
			if end in dic:
				matrix = connect(start,end,matrix,dic)
			c+=1
		for z in matrix:
			for g in z:
				print(g,end='')
			print()
		matrix = []
		dic = {}

x = 0
y = 0
c = 0
nodes = list(dic.keys())
#print(nodes)
while c<len(nodes):
	start = nodes[c]
	if ord(start)< 65:
		if start == '9':
			end = 'a'
		else:
			end = chr(ord(start)+1)
	elif ord(start) < 97:
		if start == 'Z':
			end = -1
		else:
			end = chr(ord(start) + 1)
	else:
		if start == 'z':
			end = 'A'
		else:
			end = chr(ord(start) + 1)
	#print(start,end)
	if end in dic:
		matrix = connect(start,end,matrix,dic)
	c+=1
for z in range(len(matrix)):
	for g in matrix[z]:
		print(g,end='')
	if z<(len(matrix)-1):
		print()
