import numpy as np
import torch

class Agent:
    def __init__(self, board, color, alpha=0.15, random_factor=0.15):
        self.state_history = [(0,0), 0]
        self.alpha = alpha
        self.random_factor = random_factor
        self.color = color
        self.board_state = np.zeros(board.size,board.size,8)
        self.rewards = 0

    def convert_board(self, board):
        
        #rank_sum = 0
        #piece_sum = 0
        #op_sum = 0
        #op_rank_sum = 0
        for i in board.board_size:
            for j in board.board_size:
                p = board.get_piece_from_pos((i,j))
                if p is not None:
                    if p.color == self.color:
                        #piece_sum+=1
                        #rank_sum+=p.rank
                        if p.notation == 'W':
                            self.board_state[i,j,0] = p.rank
                        elif p.notation == 'A':
                            self.board_state[i,j,1] = p.rank
                        elif p.notation == 'F':
                            self.board_state[i,j,2] = p.rank
                        elif p.notation == 'E':
                            self.board_state[i,j,3] = p.rank

                    else:
                        #op_sum+=1
                        #op_rank_sum+=p.rank
                        if p.notation == 'W':
                            self.board_state[i,j,4] = p.rank
                        elif p.notation == 'A':
                            self.board_state[i,j,5] = p.rank
                        elif p.notation == 'F':
                            self.board_state[i,j,6] = p.rank
                        elif p.notation == 'E':
                            self.board_state[i,j,7] = p.rank

        #self.rewards = (rank_sum + piece_sum) - (op_sum + op_rank_sum)
    
    def try_moving(self, board):
        square_from = board.size * board.size
        square_to = board.size * board.size


