
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
        
def print_tree_from_dict(tree: {str: (int, int)}):
    rows_of_tree = []
    for c in tree.items():
        for i in range(len(rows_of_tree), c[1][0] + 1):
            rows_of_tree.append([])
        rows_of_tree[c[1][0]].append((c[0], c[1][1]))
    
    for row in rows_of_tree:
        cols_of_output_line = []
        for node in row:
            for i in range(len(cols_of_output_line), node[1] + 1):
                cols_of_output_line.append(' ')
            cols_of_output_line[node[1]] = node[0]
        print(''.join(cols_of_output_line))
        

# numpy and scipy are available for use
# import numpy
# import scipy

def return_dict(infix,prefix):
    dic = {}
    tree = {}
    left_right = {}
    for i in range(len(infix)):
        dic[infix[i]] = [-1,i]
    dic[prefix[0]][0] = 0
    tree[prefix[0]] = [infix.index(prefix[0]),-1,-1]
    for j in range(1,len(prefix)):
        tba = prefix[j]
        index = infix.index(tba)
        start_node = prefix[0]
        while True:
            cur_check = tree[start_node]
            if index > cur_check[0]:
                if cur_check[2] != -1:
                    start_node = cur_check[2]
                else:
                    tree[start_node][2] = tba
                    tree[tba] = [index,-1,-1]
                    dic[tba][0] = dic[start_node][0]+1
                    break
            else:
                if cur_check[1] != -1:
                    start_node = cur_check[1]
                else:
                    tree[start_node][1] = tba
                    tree[tba] = [index,-1,-1]
                    dic[tba][0] = dic[start_node][0] + 1
                    break  
    print(dic) 
    return dic

while True:
    try:
        infix = get_word()
        prefix = get_word()
        dic = return_dict(infix,prefix)
        print_tree_from_dict(dic)
    except EOFError:
        break

#kaloo = {'a': (0,0), 'd': (2,3), 'b': (1,2), 'c': (2,1)}
