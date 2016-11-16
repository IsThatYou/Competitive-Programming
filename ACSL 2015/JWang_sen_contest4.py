''' put the input into a text file as follows:

1. #, aac, acc, abc, ac, abbc, abbbc, abbbbc, aabc, aabbc
2. a.c
3. a[ab]c
4. a[^ab]c
5. ab*c
6. a.b{2,4}c

then name
'''
import re
f = open("input.txt", "r")
output_count = 0
the_list = []
for i in f.readlines():
    line = i[3:]
    if output_count == 0:

        line = line.split(", ")
        if "#" in line:
            line[line.index('#')] = ''

        if "\n" in line[-1]:
            line[-1] = line[-1][:-1]

        the_list = line
        print the_list
        output_count += 1
    else:
        #get rid of '\n'
        if "\n" in line[-1]:
            line = line[:-1]

        trans = str(line)
        collection = []
        for j in the_list:
            obj = re.match(trans, j)
            if obj != None:

                if obj.group() == j:
                    collection.append(obj.group(0))


        if len(collection) != 0:
            for z in range(len(collection)):
                if collection[z] == '':
                    collection[z] = '#'
            print str(output_count) + '. ' + ', '.join(collection)
        else:
            print str(output_count) + '. ' + 'None'
        output_count += 1