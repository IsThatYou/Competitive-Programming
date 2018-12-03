def bfs(dic,s):

    maps = [0] * len(s)
    all_A=[]
    for i in range(len(s)):
        if maps[i] == 0 and s[i] == "A":
            visited, queue = set(), [i]
            while queue:
                vertex = queue.pop(0)
                if vertex<len(s):
                    if vertex not in visited and s[vertex] == "A":
                        visited.add(vertex)
                        maps[vertex] = 1
                        if i in dic:
                            for i in dic[vertex]:
                                if i not in visited:
                                    queue.append(i)
            all_A.append(visited)
    return all_A
n = int(input())
# print(ord("A"))
# print(ord("Z"))
for i in range(n):
    ans = 0
    s = list(input().strip())
    #print(s)
    if "A" not in s:
        for j in range(len(s)):
            ans += min(ord(s[j])-65,91-ord(s[j]))
            ans += 1
        ans = ans-1
        print(ans)
    else:
        ans = 0
        for j in range(len(s)):
             ans += min(ord(s[j])-65,91-ord(s[j]))


        # dic = {}
        # for i in range(1,len(s)-1):
        #     dic[i] = [i-1,i+1]
        # dic[0] = [len(s)-1,1]
        # dic[len(s)-1] = [len(s)-2,1]
        # #print(dic)
        # all_A = bfs(dic,s)

        # A_clu = all_A[0]
        # for j in all_A:
        #     if len(j)>len(A_clu):
        #         A_clu = j

        # if 0 in A_clu:
        #     A_clu = list(A_clu)
        #     A_clu = sorted(A_clu)
        #     ind1 = 0
        #     ind2 = 0 
        #     for j in range(len(A_clu)):
        #         if j != A_clu[j]:
        #             ind1 = j
        #             break
        #     count =len(s)-1
        #     for j in range(len(A_clu)-1,-1,-1):
        #         #print(count,A_clu)
        #         if count != A_clu[j]:
        #             ind2 = count
        #             break
        #         count-=1
        #     #print(ind1,ind2)
        #     l_r = ind2
        #     r_l = len(s)-ind1
        #     if min(l_r,r_l) < len(s)-1:
        #         ans += min(l_r,r_l)
        #     else:
        #         ans += len(s) -1 
        # else:
        #     l_r = len(s) - 1 - max(A_clu)
        #     r_l = min(A_clu) -1 
        #     if (min(l_r,r_l)*2 +max(l_r,r_l)) < len(s)-1:
        #         ans += min(l_r,r_l) * 2 + max(l_r,r_l)
        #     else:
        #         ans += len(s) -1 

        sums = ans
        ans += len(s) -1
        for ii in range(1, len(s)):
            if (s[ii] == 'A'):
                for j in range(ii+1,len(s)+1):
                    if s[j-1] == "A":
                        ans = min(ans, sums + min(((ii - 1) * 2) + len(s) - j, ((len(s) - j) * 2) + ii - 1));
                    else:
                        break
            

        print(ans)




