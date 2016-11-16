''' put the input into a text file as follows:

1. 0, 5, 2, 6
2. 1, 7, 3, 0
3. 2, 4, 1, 5
4. 4, 2, 3, 4
5. 4, 5, 6, 7

then name the file input.txt.
'''
f = open("input.txt", "r")
output_count = 1
for i in f.readlines():
    line = i[3:]
    line = line.split(", ")
    #get rid of '\n'
    if "\n" in line[-1]:
        line[-1] = line[-1][:1]

    new = []
    for i in line[1:]:
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
                    if special == '1' and i == 0:
                        #the first number is 1, and it is the owner.
                        apprent_list = apprent_list +'s'
                    elif special == '2' and i == 1:
                        #the first number is 2, and it is the group.
                        apprent_list = apprent_list +'s'
                    elif special == '4' and i == 2:
                        #the first number is 4, and it is the others.
                        apprent_list = apprent_list +'t'
                    else:
                        apprent_list = apprent_list +'x'
                else:
                    apprent_list = apprent_list +'-'
        new2.append(apprent_list)

    print str(output_count) + '. ' + ' '.join(new) + ' and ' + ' '.join(new2)
    output_count = output_count + 1


