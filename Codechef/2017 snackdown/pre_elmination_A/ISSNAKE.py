t = int(input())
for i in range(t):
    n = int(input())
    f = list(input())
    s = list(input())
    first = True
    first1 = False
    start = 0
    for j in range(n):
        if f[j] == '#':
            start = j
            if s[j] == '#':
                first1 = True
            break
        elif s[j] =='#':
            start = j
            first = False
            break
    count = 0
    for j in range(n):
        if f[j] == '#':
            count += 1
        if s[j] =='#':
            count += 1
    count1 = count
    f1 = list(f)
    s1 = list(s)

    start1 = start
    printit = False
    while True:
        if first:
            if count == 1:
                printit = True
                break
            a = s[start]
            if a == '#':
                count-=1
                first = False
                f[start] = '.'

            else:
                if start+1 >= n:
                    printit = False
                    break
                b = f[start+1]
                if b == "#":
                    f[start] = '.'
                    start += 1
                    count-=1

                else:
                    printit = False
                    break
        else:
            if count == 1:
                printit = True
                break
            a = f[start]
            if a == '#':
                first = True
                count-=1
                s[start] = '.'

            else:
                b = s[start + 1]
                if b == "#":
                    s[start] = '.'
                    start += 1
                    count-=1

                else:
                    printit = False
                    break
    if printit:
        print("yes")
    else:
        first = False
        if first1:
            while True:
                if first:
                    if count1 == 1:
                        printit = True
                        break
                    a = s1[start1]
                    if a == '#':
                        count1 -= 1
                        first = False
                        f1[start1] = '.'

                    else:
                        if start1 + 1 >= n:
                            printit = False
                            break
                        b = f1[start1 + 1]
                        if b == "#":
                            f1[start1] = '.'
                            start1 += 1
                            count1 -= 1

                        else:
                            printit = False
                            break
                else:
                    if count1 == 1:
                        printit = True
                        break
                    a = f1[start1]
                    if a == '#':
                        first = True
                        count1 -= 1
                        s1[start1] = '.'

                    else:
                        b = s1[start1 + 1]
                        if b == "#":
                            s1[start1] = '.'
                            start1 += 1
                            count1 -= 1

                        else:
                            printit = False
                            break

        if printit:
            print("yes")
        else:
            print("no")