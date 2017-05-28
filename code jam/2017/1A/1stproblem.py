a = open('A-large.in', 'r')
first = True
counter = 1
counter2 = 1
result = []
counter3 = 0
r =0
c=0
b = open("out.txt", "w")
for i in a:
    if first:
        t = int(i.strip())
        first = False
    else:
        if counter == counter2:
            new = [list(z) for z in result]
            for er in range(r):
                for ec in range(c):
                    if result[er][ec] != '?':
                        a1 = 0
                        a2 = r-1
                        for er2 in range(er-1,-1,-1):
                            if new[er2][ec] !='?':
                                a1 = er2+1
                                break
                        for er2 in range(er+1,r):
                            if new[er2][ec] != '?':
                                a2 = er2 - 1
                                break

                        length = 0
                        stop = False
                        for ec2 in range(ec, c):
                            for z in range(a1,a2+1):
                                if new[z][ec2] != '?' and (new[z][ec2]!=result[er][ec]):
                                    stop = True
                                    break

                            length+=1
                            if stop:
                                break
                            for z in range(a1, a2 + 1):
                                new[z][ec2] = result[er][ec]
                        if counter3 == 4:
                            print("ec:", ec)
                        stop = False
                        for ec2 in range(ec, -1,-1):
                            for z in range(a1, a2 + 1):
                                #if counter3 == 4:
                                    #print(new[z][ec2], z,ec2, result[er][ec])
                                if new[z][ec2] != '?' and (new[z][ec2] != result[er][ec]):
                                    stop = True

                                    break

                            length += 1
                            if stop:
                                break

                            for z in range(a1, a2 + 1):
                                new[z][ec2] = result[er][ec]
                        #print(a1,a2,length)
                        if counter3 == 4:
                            print(new)
            wrong = False
            for er in new:
                for ec in er:
                    if ec == "?":
                        wrong = True
                        break
                if wrong:
                    break

            if wrong:
                new = [list(z) for z in result]
                for er in range(r-1, -1,-1):
                    for ec in range(c):
                        if result[er][ec] != '?':
                            a1 = 0
                            a2 = r - 1
                            for er2 in range(er - 1, -1, -1):
                                if new[er2][ec] != '?':
                                    a1 = er2 + 1
                                    break
                            for er2 in range(er + 1, r):
                                if new[er2][ec] != '?':
                                    a2 = er2 - 1
                                    break

                            length = 0
                            stop = False
                            for ec2 in range(ec, c):
                                for z in range(a1, a2 + 1):
                                    if new[z][ec2] != '?' and (new[z][ec2] != result[er][ec]):
                                        stop = True
                                        break

                                length += 1
                                if stop:
                                    break
                                for z in range(a1, a2 + 1):
                                    new[z][ec2] = result[er][ec]
                            if counter3 == 4:
                                print("ec:", ec)
                            stop = False
                            for ec2 in range(ec, -1, -1):
                                for z in range(a1, a2 + 1):
                                    # if counter3 == 4:
                                    # print(new[z][ec2], z,ec2, result[er][ec])
                                    if new[z][ec2] != '?' and (new[z][ec2] != result[er][ec]):
                                        stop = True

                                        break

                                length += 1
                                if stop:
                                    break

                                for z in range(a1, a2 + 1):
                                    new[z][ec2] = result[er][ec]
                            # print(a1,a2,length)
                            if counter3 == 4:
                                print(new)
            result = new
            #print(result)
            if result != []:
                b.write("Case #" + str(counter3) + ": \n" + '\n'.join([''.join(z) for z in result]) + "\n")
            r, c = [int(j) for j in i.split()]
            counter2 += r + 1
            result = []
            counter3 += 1
            print(counter3)
        else:
            result.append(i.strip())
        #print(counter)
        counter += 1
new = [list(z) for z in result]
for er in range(r):
    for ec in range(c):
        if result[er][ec] != '?':
            a1 = 0
            a2 = r - 1
            for er2 in range(er - 1, -1, -1):
                if new[er2][ec] != '?':
                    a1 = er2 + 1
                    break
            for er2 in range(er + 1, r):
                if new[er2][ec] != '?':
                    a2 = er2 - 1
                    break

            length = 0
            stop = False
            for ec2 in range(ec, c):
                for z in range(a1, a2 + 1):
                    if new[z][ec2] != '?' and (new[z][ec2] != result[er][ec]):
                        stop = True
                        break

                length += 1
                if stop:
                    break
                for z in range(a1, a2 + 1):
                    new[z][ec2] = result[er][ec]
            for ec2 in range(ec, -1,-1):
                for z in range(a1, a2 + 1):
                    if new[z][ec2] != '?' and (new[z][ec2] != result[er][ec]):
                        stop = True
                        break

                length += 1
                if stop:
                    break
                for z in range(a1, a2 + 1):
                    new[z][ec2] = result[er][ec]
            # print(new)
            print(a1, a2, length)
wrong = False
for er in new:
    for ec in er:
        if ec == "?":
            wrong = True
            break
    if wrong:
        break

if wrong:
    new = [list(z) for z in result]
    for er in range(r - 1, -1, -1):
        for ec in range(c):
            if result[er][ec] != '?':
                a1 = 0
                a2 = r - 1
                for er2 in range(er - 1, -1, -1):
                    if new[er2][ec] != '?':
                        a1 = er2 + 1
                        break
                for er2 in range(er + 1, r):
                    if new[er2][ec] != '?':
                        a2 = er2 - 1
                        break

                length = 0
                stop = False
                for ec2 in range(ec, c):
                    for z in range(a1, a2 + 1):
                        if new[z][ec2] != '?' and (new[z][ec2] != result[er][ec]):
                            stop = True
                            break

                    length += 1
                    if stop:
                        break
                    for z in range(a1, a2 + 1):
                        new[z][ec2] = result[er][ec]
                if counter3 == 4:
                    print("ec:", ec)
                stop = False
                for ec2 in range(ec, -1, -1):
                    for z in range(a1, a2 + 1):
                        # if counter3 == 4:
                        # print(new[z][ec2], z,ec2, result[er][ec])
                        if new[z][ec2] != '?' and (new[z][ec2] != result[er][ec]):
                            stop = True

                            break

                    length += 1
                    if stop:
                        break

                    for z in range(a1, a2 + 1):
                        new[z][ec2] = result[er][ec]
                # print(a1,a2,length)
                if counter3 == 4:
                    print(new)
b.write("Case #" + str(counter3) + ": \n" + '\n'.join([''.join(z) for z in new]) + "\n")
a.close()
b.close()