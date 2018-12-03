#didn't use the bitise operation
#thus it is much slower and longer
def main():
    a = open('B-small-attempt1.in', 'r')
    test = a.read()
    #test = raw_input()
    test2 = test.replace('\n', ',')
    allinfo = test2.split(',')
    testcase = int(allinfo[0])
    bc = open('result1','w')
    
    for i in range(testcase):
        lis = allinfo[i + 1]
        lis = lis.split(' ')
        Aa = lis[0]
        Bb = lis[1]
        Kk = lis[2]
        Klist = list(xrange(int(Kk)))
        counter = 0
        
        
        
        for q in range(int(Aa)):
            for k in range(int(Bb)):
                newi = "{0:b}".format(q)
                newb = "{0:b}".format(k)
                lena = len(newi)
                lenb = len(newb)
                if lena < lenb:
                    newi = newi.zfill(lenb)
                elif len(newi) > len(newb):
                    newb = newb.zfill(lena)
                
                combine = []
                
                for a,b in zip(range(lena),range(lenb)):
                    if newi[a] == newb[b]:
                        if int(newi[a]) == 1:
                            combine.append('1')
                        elif int(newi[a]) == 0:
                            combine.append('0')
                    else:
                        combine.append('0')
                
                
                if len(combine) == 1:
                    dec = int(combine[0],2)
                    for number in Klist:
                        
                        if dec == number:
                            
                            counter += 1
                else:
                    combine2 = ''.join(combine)
                    deca = int(combine2, 2)
                    for number in Klist:
                        
                        if deca == number:
                            counter += 1
        
        #print ("Case #%d: %d\n" % (i + 1, counter))
        bc.write("Case #%d: %d\n" % (i+1, counter))
            
main()

                   
                        
                
        
