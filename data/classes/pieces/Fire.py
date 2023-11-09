# /* Bishop.py

import pygame
from data.classes.Piece import Piece

class Fire(Piece):
    def __init__(self, pos, color, rank, board):
        super().__init__(pos, color, rank, board)
        
        self.color = color
        img_path = 'data/imgs/' + self.color[0] + '_fire0.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'F'
        self.rank = rank
        self.strength = 'A'
        self.weak  = 'E'

    def upgrade(self,board):
        img_path = 'data/imgs/' + self.color[0] + '_fire'+str(self.rank-1)+'.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

    def get_possible_moves(self, board):
        output = []
        moves_ne = []
        for i in range(1, self.rank+1):
            if self.x + i > 4 or self.y - i < 0:
                break
            moves_ne.append(board.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)
        moves_se = []
        for i in range(1, self.rank+1):
            if self.x + i > 4 or self.y + i > 4:
                break
            moves_se.append(board.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)
        moves_sw = []
        for i in range(1, self.rank+1):
            if self.x - i < 0 or self.y + i > 4:
                break
            moves_sw.append(board.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)
        moves_nw = []
        for i in range(1, self.rank+1):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_nw.append(board.get_square_from_pos(
                (self.x - i, self.y - i)
            ))

        moves_east = []
        moves_west = []
        if self.color=='black':
            if self.pos[1] == board.board_size-1:
                moves_west = []
                for x in range(self.x-1-(self.rank-1),self.x)[::-1]:
                    if x >= 0:
                        moves_west.append(board.get_square_from_pos(
                            (x, self.y)
                        ))
                for x in range(self.x + 1, self.x + self.rank + 1):
                    if x < 5:
                        moves_east.append(board.get_square_from_pos(
                            (x, self.y)
                    ))
        else:
            if self.pos[1]  == 0:
                for x in range(self.x-1-(self.rank-1),self.x)[::-1]:
                    if x >= 0:
                        moves_west.append(board.get_square_from_pos(
                            (x, self.y)
                        ))
                for x in range(self.x + 1, self.x + self.rank + 1):
                    if x < 5:
                        moves_east.append(board.get_square_from_pos(
                            (x, self.y)
                    ))
        output.append(moves_east)
        output.append(moves_west)

        output.append(moves_nw)
        return output