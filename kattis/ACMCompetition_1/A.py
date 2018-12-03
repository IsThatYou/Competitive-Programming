n = input()
w_count = 0
b_count = 0
for i in n:
    if i == "W":
        w_count+=1
    else:
        b_count+=1
if w_count == b_count:
    print(1)
else:
    print(0)
