a = open('B-large.in', 'r')
first = True
counter = 1
b = open("out.txt", "w")
for i in a:
    if first:
        t = int(i.strip())
        first = False
    else:
        n = i.strip()
        last = 0
        new = ''
        remo = -1

        prolong = False
        for j in range(len(n)):
            if (last > int(n[j])):
                remo = j-1
                break
            else:
                new += n[j]
                last = int(n[j])
        else:
            prolong = True
        if not prolong:
            last2 = int(n[remo])
            mem = remo
            for j in range(remo-1, -1,-1):
                if int(n[j]) == last2:
                    last2 = int(n[j])
                else:
                    mem = j+1
                    break
            else:
                mem = 0
            smh = ''
            for j in range(len(n)):
                if j == mem:
                    smh += str(int(n[j]) - 1)
                elif j > mem:
                    smh += '9'
                else:
                    smh += n[j]

            b.write("Case #" + str(counter) + ": " + str(int(smh)) + "\n")
        else:
            b.write("Case #" + str(counter) + ": " + n + "\n")
        counter+=1
a.close()
b.close()