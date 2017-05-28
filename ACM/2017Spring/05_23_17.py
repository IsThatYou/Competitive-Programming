#https://www.hackerrank.com/challenges/flipping-the-matrix <-- finished, greedy
#https://www.hackerrank.com/challenges/an-interesting-game-1 <<-- finished, linear
#https://www.hackerrank.com/challenges/new-year-chaos
def f():
    q = int(input())
    for i in range(q):
        n = int(input())
        arr = []
        for j in range(2*n):
            row = [int(z) for z in input().split()]
            arr.append(row)
        sums = 0
        for j in range(n):
            for k in range(n):
                a1 = arr[j][k]
                a2 = arr[j][2*n-1-k]
                a3 = arr[2*n-1-j][k]
                a4 = arr[2*n-1-j][2*n-1-k]
                sums += max(a1,a2,a3,a4)
        print(sums)

#f()
def s():
    g = int(input())
    for i in range(g):
        n = int(input())
        arr = [int(j) for j in input().split()]
        times = 0
        nums = 0
        for j in arr:
            if j >nums:
                nums = j
                times += 1
        if times % 2:
            print("BOB")
        else:
            print("ANDY")



#s()
def t():

t()