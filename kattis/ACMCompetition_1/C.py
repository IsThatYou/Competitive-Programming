x,y = [int(x) for x in input().split()]
n = int(input())
a = {"Forward":0,"Left":1,"Right":2}
instru = []
for i in range(n):
    ins = input()
    instru.append(a[ins])
dx = 0
dy = 0
curdir = "up"
dp = []
for i in range(len(instru)):
    dp.append((dx,dy))
    if i == 0:
        if curdir == "up":
            dy += 1

        elif curdir == "left":
            dx -= 1
        elif curdir == "right":
            dx += 1
        else:
            dy -= 1
    elif i == 1:
        if curdir == "up":
            curdir = "left"
        elif curdir == "left":
            curdir = "down"
        elif curdir == "right":
            curdir = "up"
        else:
            curdir = "right"
    elif i == 2:
        if curdir == "up":
            curdir = "right"
        elif curdir == "left":
            curdir = "up"
        elif curdir == "right":
            curdir = "down"
        else:
            curdir = "left"
lis = [0,1,2]
for i in range(len(instru)):
    for j in lis:

        if j != instru[i]:
            cx,cy = dp[i]
            dx = x-cx
            dy = y-xy
            if instru[i] == 0:
                
        
print(dx,dy)        
