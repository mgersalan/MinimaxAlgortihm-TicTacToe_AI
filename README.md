# MinimaxAlgortihm-TicTacToe_AI

Given a state of the game, the algorithm simply computes the values of the children of the given state and chooses 
the one that has the maximum value if it is Max's turn, and the one that has the minimum value if it is Min's turn.

Inputs: current_board_position, who_plays
Outpus: Predicting who is going to win (Min or Max), best possible move.

Pseudocode:

1:  max_value(node):
2:     if end_state(node): return value(node)
3:     v = -Inf
4:     for each child in node.children():
5:        v = max(v, min_value(child))
6:     return v  

1:  min_value(node):
2:     if end_state(node): return value(node)
3:     v = +Inf
4:     for each child in node.children():
5:        v = min(v, max_value(child))
6:     return v 
