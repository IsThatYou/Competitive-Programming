cases = int(input())
for i in range(cases):
    ballons = []
    for q in range(10):
        ballons.append(set('rgb'))
    print(ballons)
    space = input()
    num = input().split()

    question_num = int(num[0])
    lie_num = int(num[1])
    print(question_num, lie_num)
    color_numbers = {'r':0, 'g': 0, 'b': 0}
    f_color_numbers = {'r':[0], 'g': [0], 'b': [0]}
    orlist = []

    print(color_numbers['r'])
    for j in range(question_num):
        question = input()
        answer = input()

        type = ''
        if "and" in question:
            question = question.split(' and ')
            type = 'and'

            if answer == "yes":
                for que in range(len(question)):
                    if question[que].startswith('color'):
                        index = question[que].split()[1]
                        color = question[que].split()[2]
                        ballons[index] =  color
                    elif question[que].startswith('count'):
                        color = question[que].split()[1]
                        number = question[que].split()[2]
                        color_numbers[color] = number
            elif answer == "no":
                for que in range(len(question)):
                    if question[que].startswith('color'):
                        index = question[que].split()[1]
                        color = question[que].split()[2]
                        ballons[index] = ballons[index] ^ set(color)
                    elif question[que].startswith('count'):
                        color = question[que].split()[1]
                        number = question[que].split()[2]
                        f_color_numbers[color].append(number)


        elif "or" in question:
            question = question.split(' or ')
            type = 'or'
            question.append(answer)

        else:
            if answer == "yes":
                if question[que].startswith('color'):
                    index = question[que].split()[1]
                    color = question[que].split()[2]
                    ballons[index] = color
                elif question[que].startswith('count'):
                    color = question[que].split()[1]
                    number = question[que].split()[2]
                    color_numbers[color] = number
            elif answer == 'no':
                if question[que].startswith('color'):
                    index = question[que].split()[1]
                    color = question[que].split()[2]
                    ballons[index] = ballons[index] ^ set(color)
                elif question[que].startswith('count'):
                    color = question[que].split()[1]
                    number = question[que].split()[2]
                    f_color_numbers[color].append(number)

    for o in orlist:
        ans = o[-1]
        if ans == 'no':
            for que in range(len(o) - 1):
                if question[que].startswith('color'):
                    index = question[que].split()[1]
                    color = question[que].split()[2]
                    ballons[index] = ballons[index] ^ set(color)
                elif question[que].startswith('count'):
                    color = question[que].split()[1]
                    number = question[que].split()[2]
                    f_color_numbers[color].append(number)
        elif ans == 'yes':
            for que in range(len(o) - 1):
                if question[que].startswith('color'):
                    












