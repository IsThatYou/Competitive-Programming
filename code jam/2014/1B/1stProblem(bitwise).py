#using bitwise operation
def main():
    myFile = open('B-small-attempt1.in', 'r')
    #test = raw_input()
    testcase = int(myFile.readline())
    bc = open('result1','w')

    for i in range (1, testcase + 1):
        newline = myFile.readline()
    
        A, B, K = [int(x) for x in newline.split()]
        winning_case = 0
        for a in range(A):
            for b in range(B):
                if a & b < K:
                    winning_case += 1

        print("Case #{0}: {1}".format(i, winning_case))
        

    
main()
