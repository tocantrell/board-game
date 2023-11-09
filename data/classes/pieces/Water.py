# /* Rook.py

import pygame

from data.classes.Piece import Piece

class Water(Piece):
    def __init__(self, pos, color, rank, board):
        super().__init__(pos, color, rank, board)
        img_path = 'data/imgs/' + color[0] + '_water0.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'W'
        self.rank = rank
        self.strength = 'E'
        self.weak  = 'A'

    def upgrade(self,board):
        img_path = 'data/imgs/' + self.color[0] + '_water'+str(self.rank-1)+'.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

    def get_possible_moves(self, board):
        output = []
        moves_north = []
        for y in range(self.y-1-(self.rank-1),self.y)[::-1]:
            if y >=0:
                moves_north.append(board.get_square_from_pos(
                    (self.x, y)
                ))
        output.append(moves_north)
        moves_east = []
        for x in range(self.x + 1, self.x + self.rank + 1):
            if x < 5:
                moves_east.append(board.get_square_from_pos(
                    (x, self.y)
            ))
        output.append(moves_east)
        moves_south = []
        for y in range(self.y + 1, self.y + self.rank+1):
            if y < 5:
                moves_south.append(board.get_square_from_pos(
                    (self.x, y)
                ))
        output.append(moves_south)
        moves_west = []
        for x in range(self.x-1-(self.rank-1),self.x)[::-1]:
            if x >= 0:
                moves_west.append(board.get_square_from_pos(
                    (x, self.y)
                ))
        output.append(moves_west)
        return output