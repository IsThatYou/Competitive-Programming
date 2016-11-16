''' put the input into a text file as follows:

1. 9, 17, 22, 26, 4, A, 7, C, 18, C, 19, C, 32
2. 11, 16, 20, 27, 4, A, 7, B, 19, A, 24, B, 30
3. 9, 14, 23, 28, 3, B, 7, C, 25, A, 30
4. 8, 15, 23, 28, 4, A, 7, C, 24, C, 33, A, 30
5. 9, 16, 23, 26, 4, A, 7, B, 19, B, 25, B, 18

then name the file input.txt.
'''

def actual_oneDtotwoD(num):
    num = num - 1
    row = num/6
    column = num - row * 6
    return row, column

def fill_the_less_obvious(grid):
    for i in range(4):
        for j in range(4):
            ele = grid[i][j]
            if ele == '0':
                col = [grid[0][j], grid[1][j], grid[2][j], grid[3][j]]
                row = grid[i]
                count = 0
                basket = ['A', 'B', 'C']
                for z in range(4):
                    if col[z] == 'A' or col[z] == 'B' or col[z] == 'C':
                        count += 1
                        if col[z] in basket:
                            basket.remove(col[z])
                    if row[z] == 'A' or row[z] == 'B' or row[z] == 'C':
                        count += 1
                        if row[z] in basket:
                            basket.remove(row[z])

                if count >= 2:
                    grid[i][j] = basket[0]
def check_finish(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == '0':
                return False
    return True




f = open("input.txt", "r")
output_count = 1
for i in f.readlines():
    line = i[3:]
    line = line.split(", ")
    if "\n" in line[-1]:
        line[-1] = line[-1][:-1]

    blocks = line[0:4]
    block_num = int(line[4])
    leadings = line[5::]
    grid = [['0', '0', '0', '0'] for x in xrange(4)]
    for i in blocks:
        pos = int(i)
        count = 0
        ##row, column = oneDtotwoD(pos, count - 2)
        row, column = actual_oneDtotwoD(pos)
        grid[row - 1][column - 1] = ''

    letter_index = 0
    for i in range(block_num):
        letter = leadings[letter_index]
        pos = int(leadings[letter_index + 1])
        row, column = actual_oneDtotwoD(pos)
        if column + 1 == 1:
            while grid[row-1][column]== "":
                column += 1
            grid[row-1][column] = letter
        if column - 1 == 4:
            while grid[row-1][column - 2]== "":
                column -= 1
            grid[row-1][column-2] = letter
        if row - 1 == 4:
            while grid[row-2][column - 1]== "":
                row -= 1
            grid[row-2][column-1] = letter
        if row + 1 == 1:
            while grid[row][column-1]== "":
                row += 1
            grid[row][column-1] = letter
        #print letter, pos
        letter_index += 2

    #print grid


    fill_the_less_obvious(grid)
    while check_finish(grid) == False:
        fill_the_less_obvious(grid)
    new = grid[0] + grid[1] + grid[2] + grid[3]

    result = ''.join(new)
    print str(output_count) + '. ' + result



    output_count += 1

