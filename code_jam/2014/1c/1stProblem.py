
from fractions import gcd
import math
def powTwoBit(number):
  return (number & (number-1) == 0) and (number != 0)
def getGeneration(numer, dem):
    isit = powTwoBit(dem)
    
   
    if isit:
        power = math.log(dem,2)
        if numer == 1:
            return power
        elif numer > 1:
            counterp = 0
            while True:
                numer2 = numer * 2
                if numer2 < dem:
                    dem = dem/2
                    counterp += 1
                elif numer2 > dem:
                    return (counterp + 1)
    else:
        return (0)
                


def main():
    a = open('A-large.in', 'r')
    test = a.read()
    #test = raw_input()
    test2 = test.replace('\n', ',')
    allinfo = test2.split(',')
    testcase = int(allinfo[0])
    bc = open('result2','w')
    for i in range(testcase):
        fraction = allinfo[i+1]
        fractionlis = fraction.split('/')
        numerater = int(fractionlis[0])
        dem = int(fractionlis[1])
        if not gcd(numerater, dem) == 1:
            cf = gcd(numerater,dem)
            numerater = numerater/cf
            dem = dem/cf
        
        answer = getGeneration(numerater,dem)
        

        if answer != 0:
            #print("Case #%d: %d\n" % (i+1, answer))
            bc.write("Case #%d: %d\n" % (i+1, answer))
        else:
            #print("Case #%d: impossible\n" % (i+1))
            bc.write("Case #%d: impossible\n" % (i+1))
            
                      

main()
