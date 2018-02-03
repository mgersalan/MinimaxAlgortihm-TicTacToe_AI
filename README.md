# MinimaxAlgortihm-TicTacToe_AI

Given a state of the game, the algorithm simply computes the values of the children of the given state and chooses 
the one that has the maximum value if it is Max's turn, and the one that has the minimum value if it is Min's turn.

Inputs: current_board_position, who_plays <br />
Outpus: Predicting who is going to win (Min or Max), best possible move <br />
*Outputs generated after running the script.

Pseudocode: <br />

1:  max_value(node): <br />
2:     if end_state(node): return value(node) <br />
3:     v = -Inf <br />
4:     for each child in node.children(): <br />
5:        v = max(v, min_value(child)) <br />
6:     return v  <br />
<br />
1:  min_value(node):<br />
2:     if end_state(node): return value(node) <br />
3:     v = +Inf <br />
4:     for each child in node.children(): <br />
5:        v = min(v, max_value(child)) <br />
6:     return v <br />
