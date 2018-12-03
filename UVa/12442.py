t = int(input())

for i in range(t):
    n = int(input())
    dic = {}
    longest = 0
    start_node = 1
    for j in range(n):
        u,v = [int(x) for x in input().split()]
        dic[u] = v
    searched = set()
    for j in range(n):
        fake_long = 0
        start = j+1
        if start in searched:
            continue
        #print("wa:" + str(j)) 
        #print(searched)
        searched.add(start)
        new = start
        detect = set()
        detect.add(new)
        while True:
            #print(new,start)
            
            if new in dic:
                
                new = dic[new]
                if new in detect:
                    break
                detect.add(new)
                searched.add(new)
                fake_long += 1
                
            else:
                break
        if fake_long>longest:
            longest = fake_long
            start_node = start
    print("Case " + str(i+1) +": " + str(start_node))

            

