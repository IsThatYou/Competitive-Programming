#https://www.hackerrank.com/challenges/climbing-the-leaderboard <<-- finished, 2-pointers
#https://www.hackerrank.com/challenges/castle-on-the-grid <<--
#https://www.hackerrank.com/challenges/down-to-zero-ii
from queue import PriorityQueue
def f():
    n = int(input().strip())
    scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
    m = int(input().strip())
    alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
    ##
    scores = set(scores)
    scores = list(scores)
    scores = sorted(scores,reverse=True)
    reme = len(scores)-1
    result = []
    for i in range(0, m):
        for j in range(reme,-1,-1):
            if alice[i] ==scores[j]:
                reme = j
                result.append(j)
                break
            elif alice[i] < scores[j]:
                reme = j
                result.append(j+1)
                break
        else:
            result.append(j)
    for i in result:
        print(i+1)
#f()
def s():
    
s()