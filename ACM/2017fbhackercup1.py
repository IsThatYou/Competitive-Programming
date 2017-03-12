import math
new = open("input.txt")
result = open("output.txt", "w", newline ="\n")
counter = 0
for i in new.readlines():
	num = 0
	if counter == 0:
		counter +=1
		num = int(i)
	else:
		inpu = i.split()
		P = int(inpu[0])
		X = int(inpu[1])
		Y = int(inpu[2])
		x = X-50
		y = Y-50
		angle = 400
		done = False
		if x == 0 or y == 0:
			if x == 0 and y != 0:
				if y > 0:
					angle = 0
				elif y < 0:
					angle = 180
			elif y == 0 and x != 0:
				if x > 0:
					angle = 90
				elif x < 0:
					angle = 270
			elif y == 0 and x == 0:
				if P > 0:
					done = True
					result.write("Case #{}: black\n".format(counter))
				else:
					done = True
					result.write("Case #{}: white\n".format(counter))
		else:
			angle = math.degrees(math.atan(y/x))
			if x < 0 and y < 0:
				angle = 270-angle
			elif x < 0 and y > 0:
				angle = 270 - angle
			elif x > 0 and y < 0:
				angle = 90 - angle
			elif x > 0 and y > 0:
				angle = 90 - angle
		distance = math.sqrt(x**2 + y**2)
		if distance > 50 and not done:
			done = True
			result.write("Case #{}: white\n".format(counter))
		elif distance < 50 and not done:
			done = True
			if angle > 360 * P*0.01:
				result.write("Case #{}: white\n".format(counter))
			else:
				result.write("Case #{}: black\n".format(counter))
		counter += 1

new.close()
result.close()

	