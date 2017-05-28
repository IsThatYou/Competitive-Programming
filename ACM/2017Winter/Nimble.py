#https://www.hackerrank.com/challenges/nimble-game-1
#use grundy numbers
cases = int(input())
for i in range(cases):
    n = int(input())
    a = input().split()
    last = 0
    for j in range(1, len(a)):
        new = 0
        if int(a[j]) % 2 == 0:
            new = 0
        else:
            new = j
        last = new^last
    if last == 0:
        print("Second")
    else:
        print("First")