# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
def coord2pos(xy,board_size):
    x = xy[0]
    y = xy[1]
    if y%2 == 0:
        x = board_size-x+1
        return (y -1) * board_size + x
    else:
        return (y -1) * board_size + x
import math
def pos2coord(pos,board_size):
    # incomplete
    y = math.ceil(pos/board_size)
    if y%2 ==0:
        x = pos-((y-1)) *board_size
        #print(x)
        x = board_size-x+1

    else:
        x = pos-((y-1)) *board_size
    return (x,y)
# numpy and scipy are available for use
#print(coord2pos((6,2),6))
#print(pos2coord(13,6))
import numpy
import scipy

board_size = get_number()
player_num = get_number()
snake_num = get_number()
snake_dic = {}
ladder_dic = {}
for i in range(snake_num):
    hx = get_number()
    hy = get_number()
    tx = get_number()
    ty = get_number()
    snake_dic[(hx,hy)] = (tx,ty)
ladder_num = get_number()
for i in range(ladder_num):
    hx = get_number()
    hy = get_number()
    tx = get_number()
    ty = get_number()
    ladder_dic[(hx,hy)] = (tx,ty)
k = get_number()
players = []
for i in range(player_num):
    players.append((0,1))
counter = 0
goal = board_size*board_size + 1
winners = set()
for roll in range(k):
    a = get_number()
    b = get_number()
    moves = a + b
    player_index = counter%player_num
    #print(player_index)
    while player_index in winners:
        counter += 1
        player_index = counter%player_num
    
    cur_player_pos = players[counter%player_num]
    if ((coord2pos(cur_player_pos,board_size)+moves)>=goal):
        winners.add(player_index)
        if len(winners) == player_num:
            break
        continue
    new_pos = pos2coord(moves+coord2pos(cur_player_pos,board_size), board_size)

    while (new_pos in snake_dic) or (new_pos in ladder_dic):
        if new_pos in snake_dic:
            new_pos = snake_dic[new_pos]
        else:
            new_pos = ladder_dic[new_pos]

    players[player_index] = new_pos
    #print(new_pos)
    counter += 1
for i in range(player_num):
    if i not in winners:
        print(i+1,players[i][0],players[i][1])
    else:
        print("{} winner".format(i+1))
