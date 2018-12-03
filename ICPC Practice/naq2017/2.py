dic = "0123456789ACDEFHJKLMNPRTVWX"
confus = {'B':'8','G':'C', 'I':'1', 'O':'0', 'Q':'0', 'S':'5', 'U':'V', 'Y':'V', 'Z':'2'}
p = int(input())
for i in range(p):
    a, num = [x for x in input().split()]
    num = list(num)
    for j in range(len(num)):
        if num[j] in confus:
            num[j] = confus[num[j]]
    
    dexi =[]
    for j in num:
        dec = dic.index(j)
        dexi.append(dec)
    sums = 0
    for j in range(8):
        sums +=dexi[j] * 27**(7-j)
    D1 = dexi[0]
    D2 = dexi[1]
    D3 = dexi[2]
    D4 = dexi[3]
    D5 = dexi[4]
    D6 = dexi[5]
    D7 = dexi[6]
    D8 = dexi[7]
    
    result = (2*D1 + 4*D2 + 5*D3 + 7*D4 + 8*D5 + 10*D6 + 11*D7 + 13*D8)%27
    if result == dexi[8]:
        print(a + " " + str(sums))
    else:
        print(a + " " + "Invalid")
    #num = ''.join(num)

    
        

