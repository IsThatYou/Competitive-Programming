# https://www.hackerrank.com/contests/rookierank-2/challenges/hackerrank-in-a-string
def HackerRank_in_a_String():
    q = int(input().strip())

    for a0 in range(q):
        s = input().strip()
        b = "hackerrank"
        for i in s:
            if len(b) == 0:
                break
            if i == b[0]:
                b = b[1:]
        if len(b) == 0:
            print("YES")
        else:
            print("NO")

#HackerRank_in_a_String()
# https://www.hackerrank.com/contests/rookierank-2/challenges/knightl-on-chessboard # unfinished
def KnightL_on_a_Chessboard():
    n = int(input().strip())
    answer = [[0]*(n-1) for i in range(n-1)]
    for a in range(1, n):
        for b in range(a, n):
            #print(a,b)
            board = [[0]*n for i in range(n)]
            board[0][0] = 1
            c = set()
            c.add((a,b,1))
            c.add((b,a,1))
            lengths = []
            while len(c) != 0:
                t = c.pop()
                if (a == 1 and b == 1) and :
                    print(t)

                board[t[0]][t[1]] =1
                if t[0] + a < n:
                    if t[1] + b < n and (board[t[0] + a][t[1] + b]>=t[2] or board[t[0] + a][t[1] + b] == 0):
                        # update the board
                        c.add((t[0] + a, t[1] + b, t[2]+1))
                    if t[1] - b >= 0 and (board[t[0] + a][t[1] - b]>=t[2] or board[t[0] + a][t[1] - b] == 0):
                        c.add((t[0] + a, t[1] - b, t[2]+1))
                if t[0] - a >= 0:
                    if t[1] + b < n and (board[t[0] - a][t[1] + b]>=t[2] or board[t[0] - a][t[1] + b] == 0):
                        c.add((t[0] - a, t[1] + b, t[2]+1))
                    if t[1] - b >= 0 and (board[t[0] - a][t[1] - b]>=t[2] or board[t[0] - a][t[1] - b] == 0):
                        c.add((t[0] - a, t[1] - b, t[2]+1))
                if t[0] + b < n:
                    if t[1] + a < n and (board[t[0] + b][t[1] + a]>=t[2] or board[t[0] + b][t[1] + a] ==0):
                        c.add((t[0] + b, t[1] + a, t[2]+1))
                    if t[1] - a >= 0 and (board[t[0] + b][t[1] - a]>=t[2] or board[t[0] + b][t[1] - a] ==0):
                        c.add((t[0] + b, t[1] - a, t[2]+1))
                if t[0] - b >= 0:
                    if t[1] + a < n and (board[t[0] - b][t[1] + a]>=t[2] or board[t[0] - b][t[1] + a] == 0):
                        c.add((t[0] - b, t[1] + a, t[2]+1))
                    if t[1] - a >= 0 and (board[t[0] - b][t[1] - a]>=t[2] or board[t[0] - b][t[1] - a] == 0):
                        c.add((t[0] - b, t[1] - a, t[2]+1))

                if (t[0] == n-1 and t[1] == n-1):
                    lengths.append(t[2])

            if board[-1][-1]:
                answer[a-1][b-1] = min(lengths)
                answer[b-1][a-1] = min(lengths)
            else:
                answer[a-1][b-1] = -1
                answer[b-1][a-1] = -1
    for i in answer:
        for j in i:
            print(j, end=' ')
        print()



KnightL_on_a_Chessboard()
# https://www.hackerrank.com/contests/rookierank-2/challenges/prefix-neighbors
# unfinished