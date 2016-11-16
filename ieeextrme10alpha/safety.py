password = input()
cases = int(input())
ipassword = password
for case in range(cases):
    comm = input().split()
    if comm[0] == '1':
        i = int(comm[1])
        j = int(comm[2])
        k = int(comm[3])
        if ipassword[i-1:j] == ipassword[k-1:k+j-i]:
            print('Y')
        else:
            print('N')
    elif comm[0] == '2':
        i = int(comm[1])
        j = int(comm[2])
        k = int(comm[3])
        replace = ipassword[k-1:k+j-i]
        s = ''.join([ipassword[0: i-1],replace,ipassword[j:]])
        ipassword = s
    elif comm[0] == '3':
        i = int(comm[1])
        j = int(comm[2])
        replace = ipassword[i-1:j]
        new = ''
        for z in replace:
            if z != 'z':
                num = ord(z) + 1
                new_s = chr(num)
                new += new_s
            else:
                new += 'a'

        s = ''.join([ipassword[0:i - 1],new,ipassword[j:]])
        ipassword = s

