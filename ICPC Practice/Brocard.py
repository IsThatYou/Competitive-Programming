import sys
import math

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def get_new(vector, b_angle):
	'''
	angle_ab = 0
	if vector[0] == 0:
		if vector[1] > 0:
			angle_ab = math.pi/2.0
		elif vector[1] < 0:
			angle_ab = 3 * math.pi/2.0
	elif vector[1] == 0:
		if vector[0] > 0:
			angle_ab = 0
		elif vector[0] < 0:
			angle_ab = math.pi
	else:
		#angle = math.atan(vector[1]/vector[0])
		#new_angle= angle + b_angle
	'''
	new_vector = (vector[0] * math.cos(b_angle) - vector[1] * math.sin(b_angle), vector[0] * math.sin(b_angle) + vector[1]*math.cos(b_angle))
	return new_vector




counter = 0
casenum = 0
for case in sys.stdin:
	if counter == 0:
		casenum = case
		counter += 1
	else:
		inp = case.split()
		a = (float(inp[1]), float(inp[2]))
		b = (float(inp[3]), float(inp[4]))
		c = (float(inp[5]), float(inp[6]))
		ab = (b[0] - a[0], b[1] - a[1])
		ac = (c[0] - a[0], c[1] - a[1])
		cab = angle(ab, ac)

		ba = (a[0] - b[0], a[1] - b[1])
		bc = (c[0] - b[0], c[1] - b[1])
		abc = angle(ba, bc)

		cb = (b[0] - c[0], b[1] - c[1])
		ca = (a[0] - c[0], a[1] - c[1])
		bac = angle(cb, ca)
		
		b_angle = math.atan(1/((1/math.tan(cab)) + (1/math.tan(abc)) + (1/math.tan(bac))))

		#use dot product again.

		bro_ab = get_new(ab, b_angle)
		bro_bc = get_new(bc, b_angle)

		#line1 = (a, (bro_ab[0] + a[0], bro_ab[1] + a[1]))
		#line2= (b, (bro_bc[0] + b[0], bro_bc[1] + b[1]))
		a_slope = bro_ab[1]/bro_ab[0]
		b_slope = bro_bc[1]/bro_bc[0]

		c_constant = a[1] - a_slope * a[0]
		d_constant = b[1] - b_slope * b[0]

		px = (d_constant - c_constant)/(a_slope - b_slope)
		py = (a_slope * d_constant - b_slope * c_constant)/(a_slope - b_slope)
		print(str(counter) + ' ' + str(px) + ' ' + str(py))
		counter += 1

