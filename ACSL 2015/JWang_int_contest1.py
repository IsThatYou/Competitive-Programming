''' put the input into a text file as follows:

1. 5, 2, 6
2. 7, 3, 0
3. 100, 001, 101
4. 010, 011, 100
5. r-x, rw-, rwx

then name the file input.txt.
'''
f = open("input.txt", "r")
output_count = 1
for i in f.readlines():
    line = i[3:]

    line = line.split(", ")
    #get rid of '\n'
    if "\n" in line[-1]:
        line[-1] = line[-1][:3]

    if len(line[0]) != 3:
        new = []
        for i in line:
            binary_num = format(int(i), 'b')
            # add the extra 0 that conversion does not cover.
            if len(binary_num) != 3:
                binary_num = '0' * (3 - len(binary_num)) + binary_num
            new.append(binary_num)
        new2 = []
        special = line[0]
        for i in range(3):
            apprent_list = ''
            for j in range(3):
                if j == 0:
                    if new[i][j] == "1":
                        apprent_list = apprent_list +'r'
                    else:
                        apprent_list = apprent_list +'-'
                elif j == 1:
                    if new[i][j] == "1":
                        apprent_list = apprent_list +'w'
                    else:
                        apprent_list = apprent_list +'-'
                elif j == 2:
                    if new[i][j] == "1":
                        apprent_list = apprent_list +'x'
                    else:
                        apprent_list = apprent_list +'-'
            new2.append(apprent_list)
        print str(output_count) + '. ' + ' '.join(new) + ' and ' + ' '.join(new2)
        output_count = output_count + 1
    elif len(line[0]) == 3 and (line[0][0] == '0' or line[0][0] == '1'):
        new = line
        new2 = []
        for i in range(3):
            apprent_list = ''
            for j in range(3):
                if j == 0:
                    if new[i][j] == "1":
                        apprent_list = apprent_list +'r'
                    else:
                        apprent_list = apprent_list +'-'
                elif j == 1:
                    if new[i][j] == "1":
                        apprent_list = apprent_list +'w'
                    else:
                        apprent_list = apprent_list +'-'
                elif j == 2:
                    if new[i][j] == "1":
                        apprent_list = apprent_list +'x'
                    else:
                        apprent_list = apprent_list +'-'
            new2.append(apprent_list)
        new = []
        for i in line:
            binary_num = int(i, 2)
            octal_num = format(binary_num, 'o')
            # add the extra 0 that conversion does not cover.
            new.append(octal_num)
        print str(output_count) + '. ' + ''.join(new) + ' and ' + ' '.join(new2)
        output_count = output_count + 1

    else:
        new = []
        for i in line:
            new_binary = ''
            for j in i:
                if j == 'r':
                    new_binary = new_binary + '1'
                elif j == 'w':
                    new_binary = new_binary + '1'
                elif j == 'x':
                    new_binary = new_binary + '1'
                else:
                    new_binary = new_binary + '0'
            new.append(new_binary)
        new2 = []
        for i in new:
            binary_num = int(i, 2)
            octal_num = format(binary_num, 'o')
            # add the extra 0 that conversion does not cover.
            new2.append(octal_num)
        print str(output_count) + '. ' + ''.join(new2) + ' and ' + ' '.join(new)




