matrix = [[0]*4 for i in range(4)]
for i in range(4): 
    line = [int(x) for x in input().split()]
    matrix[i][0] = line[0]
    matrix[i][1] = line[1]
    matrix[i][2] = line[2]
    matrix[i][3] = line[3]
d = int(input())
if d == 0:
    for i in range(3,-1,-1):
        for j in range(3,-1,-1):
            if matrix[i][j] != 0:
                value = matrix[i][j]
                #for j2 in range(j-1,-1,-1):
                j2 = j-1
                if j2 >=0:
                    if matrix[i][j2] == value:
                        matrix[i][j2] = value *2
                        matrix[i][j] = 0
                    elif matrix[i][j2] == 0:
                        matrix[i][j2] = value
                        matrix[i][j] = 0
                    else:
                        pass
    for i in range(3,-1,-1):
        for j in range(0,4):
            if matrix[i][j] != 0:
                value = matrix[i][j]
                for j2 in range(j-1, -1,-1):
                    if matrix[i][j2] == 0:
                        matrix[i][j2] = value
                        matrix[i][j2+1] = 0
elif d == 1:
    for j in range(3,-1,-1):
        for i in range(0,4):
            if matrix[i][j] != 0:
                value = matrix[i][j]
                for i2 in range(i-1, -1,-1):
                    if matrix[i2][j] == 0:
                        matrix[i2][j] = value
                        matrix[i2+1][j] = 0
    print(matrix)
    for j in range(3,-1,-1):
        for i in range(3,-1,-1):
            if matrix[i][j] != 0:
                value = matrix[i][j]
                #for j2 in range(j-1,-1,-1):
                i2 = i-1
                if i2 >=0:
                    if matrix[i2][j] == value:
                        matrix[i2][j] = value *2
                        matrix[i][j] = 0
                    elif matrix[i2][j] == 0:
                        matrix[i2][j] = value
                        matrix[i][j] = 0
                    else:
                        pass
print(matrix)
