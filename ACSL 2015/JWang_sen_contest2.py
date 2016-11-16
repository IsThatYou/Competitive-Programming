''' put the input into a text file as follows:

1. 523.125, 6, 2
2. +523.125, 8, 3
3. -523.163, 6, 1
4. 523.125, 4, 2
5. -523.12, 6, 1
6. -99.199, 6, 1

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
    int_num = 0
    float_num = 0
    point_index = line[0].index('.')
    float_num = len(line[0]) - point_index - 1
    int_num = point_index

    if line[0][0] == '+' or line[0][0] == '-':
        int_num = point_index - 1

    num_actual_char = point_index + 1 + int(line[2])
    num_desired_char = int(line[1])
    if num_desired_char < num_actual_char:
        print str(output_count) + '. ' + '#' * (int(line[1]) - 1 - int(line[2])) + '.' + '#' * (int(line[2]))

    # account for the case when num_desired_char > num_actual_char
    else:
        if line[0][0] != '-':
            new = line[0]
            plus = 0
            if line[0][0] == '+':
                new = new[1:]
                plus = 1

            point_index1 = new.index('.')
            determine_index = point_index1 + int(line[2]) + 1
            new1 = new[0:point_index1] + new[(point_index1+1):determine_index]
            if determine_index >= len(new):
                determine = 0
            else:
                determine = new[determine_index]

            new2 = new1
            if int(determine) >= 5:
                new2 = str(int(new1) + 1)

            if len(new2) > len(str(new1)):
                result = new2[0:(point_index1 + 1)] + '.' + new2[(point_index1 + 1):]
            else:
                result = new2[0:(point_index1)] + '.' + new2[(point_index1):]
            if len(result) + plus > num_desired_char:
                print str(output_count) + '. ' + '#' * (int(line[1]) - 1 - int(line[2])) + '.' + '#' * (int(line[2]))
                continue
            if plus == True:
                result = '+' + result

            print str(output_count) + '. ' + '#' * (num_desired_char - len(result)) + result
        elif line[0][0] == '-':
            new = line[0]
            new = new[1:]

            point_index1 = new.index('.')
            determine_index = point_index1 + int(line[2]) + 1
            new1 = new[0:point_index1] + new[(point_index1+1):determine_index]
            if determine_index >= len(new):
                determine = 0
            else:
                determine = new[determine_index]

            new2 = new1
            if int(determine) >= 5:
                new2 = str(int(new1) + 1)

            if len(new2) > len(str(new1)):
                result = new2[0:(point_index1 + 1)] + '.' + new2[(point_index1 + 1):]
            else:
                result = new2[0:(point_index1)] + '.' + new2[(point_index1):]
            if len(result) + 1 > num_desired_char:
                print str(output_count) + '. ' + '#' * (int(line[1]) - 1 - int(line[2])) + '.' + '#' * (int(line[2]))
                continue

            result = '-' + result
            print str(output_count) + '. ' + '#' * (num_desired_char - len(result)) + result




    output_count += 1
