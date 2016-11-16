import sys

def find_root(l,r):
	seq = []
	while r != 1 or l != 1:
		if l > r:
			l = l - r
			seq.append('1')
		elif l < r:
			r = r - l
			seq.append('0')

	return seq

def get_dat_row(seq):

	this_pos = 1
	for i in range(len(seq) - 1, -1, -1):
		if seq[i] == '1':
			next_pos = this_pos * 2
			this_pos = next_pos
		elif seq[i] == '0':
			next_pos = this_pos * 2 - 1
			this_pos = next_pos
	return this_pos


counter = 0
casenum = 0
for case in sys.stdin:
	if counter == 0:
		casenum = case
	else:
		data = case.split()
		number = data[1]
		l = int(number.split('/')[0])
		r = int(number.split('/')[1])
		seq = find_root(l, r)
		sums = 0
		if len(seq) > 0:
			for i in range(len(seq)):
				sums += 2**i
			pos = get_dat_row(seq)
			result = sums + pos
			print(str(counter) + ' ' + str(result))
		elif len(seq) == 0:
			print(str(counter) + ' 1')
	counter += 1

