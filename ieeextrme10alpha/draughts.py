

def find_white(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == "o":
                return [i, j]
def check_move(oboard, white ,dir):
    board = oboard
    wcol = white[1]
    wrow = white[0]
    list_b = []

    #left
    if dir == 0:
        if wcol!= 0:
            done = False
            for i in range(wcol - 1, -1, -1):
                interested = board[wrow][i]
                if not done:
                    if interested == 'x':
                        if i != 0:
                            for j in range(i - 1, -1, -1):
                                if board[wrow][j] == '.':
                                    list_b.append([wrow, j])
                                elif board[wrow][j] == 'x':
                                    done = True
                                    break
                else:
                    break

    #top
    elif dir == 1:
        if wrow!=0:
            done = False
            for i in range(wrow - 1, -1, -1):
                interested = board[i][wcol]
                if not done:
                    if interested == 'x':
                        if i != 0:
                            for j in range(i - 1, -1, -1):
                                if board[j][wcol] == '.':
                                    list_b.append([j, wcol])
                                elif board[j][wcol] == 'x':
                                    done = True
                                    break
                else:
                    break
    #right
    elif dir == 2:
        if wcol != 7:
            done = False
            for i in range(wcol+1, 8):
                interested = board[wrow][i]
                if not done:
                    if interested == 'x':
                        if i != 7:
                            for j in range(i + 1, 8):
                                if board[wrow][j] == '.':
                                    list_b.append([wrow, j])
                                elif board[wrow][j] == 'x':
                                    done = True
                                    break
                else:
                    break
    #down
    elif dir == 3:
        if wrow != 7:
            done = False
            for i in range(wrow + 1, 8):
                interested = board[i][wcol]
                if not done:
                    if interested == 'x':
                        if i != 7:
                            for j in range(i + 1, 8):
                                if board[j][wcol] == '.':
                                    list_b.append([j, wcol])
                                elif board[j][wcol] == 'x':
                                    done = True
                                    break
                else:
                    break
    return list_b

def check_move2(board, white):
    list_b = []
    wcol = white[1]
    wrow = white[0]
    #left
    if wcol > 1:
        if board[wrow][wcol-1] == 'x':
            if board[wrow][wcol-2] == '.':
                list_b.append([wrow, wcol-2])
    #top
    if wrow > 1:
        if board[wrow - 1][wcol] == 'x':
            if board[wrow - 2][wcol] ==  '.':
                list_b.append([wrow - 2, wcol])

    #right
    if wcol < 6:
        if board[wrow][wcol + 1] == 'x':
            if board[wrow][wcol + 2] == '.':
                list_b.append([wrow, wcol + 2])

    return list_b




def validmoves(board, king, eat, last):
    pos = find_white(board)
    tmoves = []
    if king:
        if not eat:
            for i in range(4):
                moves = check_move(board,pos, i)
                for j in moves:
                    tmoves.append(j)
        if eat:
            for i in range(4):
                if i != last:
                    moves = check_move(board, pos, i)
                    for j in moves:
                        tmoves.append(j)
    else:
        tmoves = check_move2(board,pos)

    return tmoves
def which_dir(old, new):
    if new[0] - old[0] == 0:
        if new[1] - old[1] > 0:
            return 0
        elif new[1] - old[1] < 0:
            return 2
    elif new[0] - old[0] > 0:
        return 1
    elif new[0] - old[0] <0:
        return 3

def win(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'x':
                return False
    return True
def del_black(oboard, origin, target):
    board = oboard[:]
    if target[0] - origin[0] == 0:
        if target[1] - origin[1] > 0:
            for i in range(origin[1]+1, target[1]):
                if board[origin[0]][i] == 'x':
                    board[origin[0]] = list(board[origin[0]])
                    board[origin[0]][i] = '.'
                    board[origin[0]] = ''.join(board[origin[0]])
        elif target[1] - origin[1] < 0:
            for i in range(target[1] + 1, origin[1]):
                if board[origin[0]][i] == 'x':
                    board[origin[0]] = list(board[origin[0]])
                    board[origin[0]][i] = '.'
                    board[origin[0]] = ''.join(board[origin[0]])

    elif target[1] - origin[1] == 0:
        if target[0] - origin[0] > 0:
            for i in range(origin[0] + 1, target[0]):
                if board[i][origin[1]] == 'x':
                    board[i] = list(board[i])
                    board[i][origin[1]] = '.'
                    board[i] = ''.join(board[i])

        elif target[0] - origin[0] < 0:

            for i in range(target[0] + 1, origin[0]):
                if board[i][origin[1]] == 'x':
                    board[i] = list(board[i])
                    board[i][origin[1]] = '.'
                    board[i] = ''.join(board[i])

    return board
def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()

def move_the_white(oboard, old, last, king):
    board = oboard
    if win(board):
        return 1

    wpos = find_white(board)
    moves = []
    #print(old, end='--')
    #print(wpos, end = ':')

    if wpos[0] == 0:
        king = True


    if last != None:
        moves = validmoves(board, king, True, last)
    else:
        moves = validmoves(board, king, False, last)

    if len(moves) == 0:
        #print("o")
        return 0

    total_i_dim = 0
    #print(moves)
    #print()
    for i in range(len(moves)):
        new_board = board[:]
        new_move = moves[i]

        new_board = del_black(new_board, wpos, new_move)
        new_board[wpos[0]] = list(new_board[wpos[0]])
        new_board[wpos[0]][wpos[1]] = '.'
        new_board[wpos[0]] = ''.join(new_board[wpos[0]])

        new_board[new_move[0]] = list(new_board[new_move[0]])
        new_board[new_move[0]][new_move[1]] = 'o'
        new_board[new_move[0]] = ''.join(new_board[new_move[0]])
        #print_board(new_board)

        last = which_dir(wpos, new_move)
        total_i_dim += move_the_white(new_board, wpos, last, king)


    return total_i_dim

cases = int(input())
for case in range(cases):
    board = []
    for i in range(8):
        row = input()
        board.append(row)
    if case+1 != cases:
        blank = input()
    wpos = find_white(board)
    a = None
    total = move_the_white(board, wpos, a, False)
    print(total)