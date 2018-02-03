import numpy as np
import time
import sys

diag_arr = np.array(['O','O','O'])
f_diag_arr = np.array(['X','X','X'])

def drawBoard(board):
    print('   |   |')
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print('   |   |')
    

def winning_row(board):
    if np.array_equal(np.diag(board),f_diag_arr) or np.array_equal(np.diag(np.fliplr(board)),f_diag_arr):
        return 1
    if np.array_equal(np.diag(board),diag_arr) or np.array_equal(np.diag(np.fliplr(board)),diag_arr):
        return -1
    for i in range (0,3):
        if (np.count_nonzero(board[i] == 'X') == 3):
            return 1
        if (np.count_nonzero(board[i] == 'O') == 3):
            return 0
        if np.count_nonzero(board[:,i] == 'X') == 3:
            return 1
        if np.count_nonzero(board[:,i] == 'O') == 3:
            return -1
    return 0



def list_of_children(board,whoplays):

    if whoplays == 'MIN':
        val = 'O'
    elif whoplays == 'MAX':
        val = 'X'
    num_of_children = np.count_nonzero(board)
    if num_of_children == 0: return 0
    index = -1
    children_list = []
    flat = board.flatten()
    for i in range(0,len(flat)):
        flat = board.flatten()
        if flat[i] == ' ':
            if i != index:
                flat[i] = val
                index = i
                children_list.append(flat.reshape((3,3)))
    return children_list



who_plays = "MIN"
current_board_position = np.array([['O','X','O'],['X',' ','X'],[' ','O',' ']])
second_pos = np.array([['O','X','O'],['X',' ','X'],[' ',' ','O']])

#print(list_of_children(current_board_position,who_plays)[0])
def win_before_terminal(node,who_started):
    if np.count_nonzero(node) != 9 and winning_row(node) and who_started =='MIN':
        return 'MAX'
    else:
        if np.count_nonzero(node) != 9 and winning_row(node) and who_started =='MAX':
            return 'MIN'
        else:
            return 'NO_CHANGE'



value_of_nodes =[]
#value_of_nodes.append((current_board_position,0))
#value_of_nodes.append((second_pos,-1))
#visited_list = [x for x, _ in value_of_nodes]
#any(np.array_equal(second_pos, x) for x in visited_list)

def best_Move(board_position,isMin):

    children_list = list_of_children(board_position,isMin)

    for each_child in children_list:
        for k in range (0,len(value_of_nodes)-1):
            if np.array_equal(each_child,value_of_nodes[k][0]):
                value = value_of_nodes[k][1]


        if isMin == 'MIN' and value == -1:
            return each_child
        elif isMin == 'MAX' and value == 1:
            return each_child

Parent_Nodes = []
def MinMax(board_position,who_starts):
    #print("Board position")
    #drawBoard(board_position)

    if winning_row(board_position) == 1 and np.count_nonzero(board_position) != 9:
        value_of_nodes.append((board_position, 1))
    if winning_row(board_position) == -1 and np.count_nonzero(board_position) != 9:
        value_of_nodes.append((board_position, -1))

    if winning_row(board_position) == 1:
        return 1
    if winning_row(board_position) == -1:
        return -1

    if winning_row(board_position) == 0:

        a = np.count_nonzero(board_position)
        if np.count_nonzero(board_position) == 9:                               ## if current board position is at terminal state
            return winning_row(board_position)

        possible_moves = list_of_children(board_position,who_starts)
        for i in possible_moves:
            Parent_Nodes.append((i,board_position))


        if who_starts == 'MAX':
            v = float('-inf')
            for child in possible_moves:
                who_starts = 'MIN'
                v = max(v, MinMax(child, who_starts))
                visited_list = [x for x, _ in value_of_nodes]
                if any(np.array_equal(child, x) for x in visited_list) == False:
                    value_of_nodes.append((child, v))
            return v

        if who_starts == 'MIN':
            v = float('inf')
            for child in possible_moves:
                who_starts = 'MAX'
                v = min(v, MinMax(child, who_starts))
                visited_list = [x for x, _ in value_of_nodes]
                if any(np.array_equal(child, x) for x in visited_list) == False:
                    value_of_nodes.append((child, v))
            return v



who_plays = 'MIN'

a = MinMax(current_board_position,who_plays)        ## enter board position

print("Initial board position \n")
drawBoard(current_board_position)                   ## enter board position
print('\n')
print(who_plays,"started ")
if a == 1:
    print("MAX Wins")
if a == -1:
    print("MIN Wins")
print("------------------")
print('\n')
print('\n')
time.sleep(0.2)
print("Best move for :",who_plays , "for below position")
drawBoard(current_board_position)                       ## enter board position
print('\n')
print("would be")
drawBoard(best_Move(current_board_position,who_plays))   ## enter board position

