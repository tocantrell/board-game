import pygame
import random

class NPC:
    def __init__(self, board, npc_color):
        self.board = board
        self.npc_color = npc_color
        self.move_count = 0
        self.last_move_type = None
        self.last_move_rank = None

    def get_piece_count(self):
        pieces = [
            i.occupying_piece for i in self.board.squares if (i.occupying_piece is not None) and (i.occupying_piece.color == self.npc_color)
        ]
        return len(pieces)

    def get_all_moves(self):
        pieces = [
            i.occupying_piece for i in self.board.squares if (i.occupying_piece is not None) and (i.occupying_piece.color == self.npc_color)
        ]
        opp_pieces = [
            i.occupying_piece for i in self.board.squares if (i.occupying_piece is not None) and (i.occupying_piece.color != self.npc_color)
        ]
        possible_moves = []
        for piece in pieces:
            moves = piece.get_moves(self.board)
            possible_moves.append(moves)

        #possible_moves_mid = []
        #for i in range(len(possible_moves)):
        #    possible_moves_mid.append([x for x in possible_moves[i] if x != []])
        #possible_moves = []
        #for i in range(len(possible_moves_mid)):
        #    possible_moves.append([x for x in possible_moves_mid[i] if x[0].pos != pieces[i].pos])
        movable_pieces = [piece for piece in pieces if any(possible_moves[pieces.index(piece)])]
        #possible_moves = [move for move in possible_moves if any(move)]
        return movable_pieces, possible_moves, opp_pieces
    
    def move_random(self, movable_pieces, possible_moves):
        piece = random.choice(movable_pieces)
        square = random.choice(possible_moves[movable_pieces.index(piece)])
        print('white')
        piece.move(self.board, square)
        self.board.turn = 'white' if self.board.turn == 'black' else 'black'
        self.move_count+=1

    def move_greedy(self, movable_pieces, possible_moves, opp_pieces):
        #Always capture weak pieces first, followed by normal capture, then random move
        #Find overlap of possible moves and opponent squares
        opp_squares = [x.pos for x in opp_pieces]
        opp_notation = [x.notation for x in opp_pieces]
        strong_moves = []
        capture_moves = []
        #print(movable_pieces)
        #print(possible_moves)
        for i in range(len(movable_pieces)):
            move_mid = [x.pos for x in possible_moves[i]]
            overlap = list(set(move_mid)&set(opp_squares))
            if len(overlap) >0:
                strength = movable_pieces[i].strength
                for j in overlap:
                    square = self.board.get_square_from_pos(j)
                    if strength == opp_notation[opp_squares.index(j)]:
                        strong_moves.append([movable_pieces[i],square])
                    else:
                        capture_moves.append([movable_pieces[i],square])
        if len(strong_moves) > 0:
            #print('strong')
            rand_index = random.choice(range(len(strong_moves)))
            piece = strong_moves[rand_index][0]
            square = strong_moves[rand_index][1]
            piece.move(self.board,square)
        elif len(capture_moves) > 0:
            #print('capture')
            rand_index = random.choice(range(len(capture_moves)))
            piece = capture_moves[rand_index][0]
            square = capture_moves[rand_index][1]
            piece.move(self.board,square)
        else:
            #print('random')
            piece = random.choice(movable_pieces)
            valid_moves = piece.get_valid_moves(self.board)
            square = random.choice(valid_moves)
            #square = random.choice(possible_moves[movable_pieces.index(piece)])
            piece.move(self.board, square)
        self.board.turn = 'white' if self.board.turn == 'black' else 'black'
        self.move_count+=1
        self.last_move_type = piece.notation
        self.last_move_rank = piece.rank