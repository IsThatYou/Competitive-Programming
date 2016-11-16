def getAnswer(n, m, k):
    

def main():
    #a = open('A-large.in', 'r')
    #test = a.read()
    test = raw_input()
    test2 = test.replace('\n', ',')
    allinfo = test2.split(',')
    testcase = int(allinfo[0])
    #bc = open('result1','w')
    for i in range (1, testcase + 1):
        group = allinfo[i]
        group2 = group.split(' ')
        n,m,k = group2
        
        
