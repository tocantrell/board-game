# /* Piece.py

import pygame
import time

class Piece:
    def __init__(self, pos, color, rank, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.rank = rank
        self.has_moved = False

    def get_moves(self, board):
        output = []
        for direction in self.get_possible_moves(board):
            for square in direction:
                if square != board.get_square_from_pos(self.pos):
                    if square.occupying_piece is not None:
                        #Handle weaknesses
                        if square.occupying_piece.notation == self.weak:
                            break
                        #if square.occupying_piece.color == self.color:
                        #    break
                        else:
                            output.append(square)
                            break
                    else:
                        output.append(square)
        return output
    
    def get_valid_moves(self, board):
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)
        return output
    
    def move(self, board, square, force=False):
        for i in board.squares:
            i.highlight = False
        if square in self.get_valid_moves(board) or force:
            prev_square = board.get_square_from_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.occupying_piece = None
            #Add logic for promotions here
            if square.occupying_piece != None:
                if square.occupying_piece.notation == self.strength:
                    self.rank+=1
                    self.upgrade(board)
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
            
            return True
        else:
            print('Problem moving!')
            board.selected_piece = None
            return False

    # True for all pieces except pawn
    def attacking_squares(self, board):
        return self.get_moves(board)