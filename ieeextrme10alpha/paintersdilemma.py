case = int(input())
for i in range(case):
    length = int(input())
    seq = input().split()
    times = 0
    brush1 = -1
    brush2 = -1
    save = 2
    for j in range(len(seq)):
        if brush1 != seq[j] and brush2 != seq[j]:
            if save == 1:
                brush2 = seq[j]
                times += 1
                for k in range(j + 1, len(seq)):
                    interest = seq[k]
                    if brush1 == interest:
                        save = 1
                        break
                    elif brush2 == interest:
                        save = 2
                        break
            else:
                brush1 = seq[j]
                times += 1
                for k in range(j + 1, len(seq)):
                    interest = seq[k]
                    if brush1 == interest:
                        save = 1
                        break
                    elif brush2 == interest:
                        save = 2
                        break
        elif brush1 == seq[j] or brush2 == seq[j]:
            for k in range(j + 1, len(seq)):
                interest = seq[k]
                if brush1 == interest:
                    save = 1
                    break
                elif brush2 == interest:
                    save = 2
                    break
            pass
    print(times)
