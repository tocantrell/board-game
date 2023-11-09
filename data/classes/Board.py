import pygame
from data.classes.Square import Square
from data.classes.pieces.Earth import Earth
from data.classes.pieces.Fire import Fire
from data.classes.pieces.Air import Air
from data.classes.pieces.Water import Water

# Game state checker
class Board:
    def __init__(self, width, height):
        self.board_size = 5
        self.width = width
        self.height = height
        self.tile_width = width // self.board_size
        self.tile_height = height // self.board_size
        self.selected_piece = None
        self.turn = 'white'
        self.config = [
            ['bE1', 'bF1', '', 'bA1', 'bW1'],
            ['bE1', 'bF1', '', 'bA1', 'bW1'],
            ['','','','',''],
            ['wW1', 'wA1', '', 'wF1', 'wE1'],
            ['wW1', 'wA1', '', 'wF1', 'wE1'],
        ]
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        output = []
        for y in range(self.board_size):
            for x in range(self.board_size):
                output.append(
                    Square(x,  y, self.tile_width, self.tile_height)
                )
        return output

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square

    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    piece_rank = int(piece[2])
                    if piece[1] == 'E':
                        square.occupying_piece = Earth(
                            (x, y), 'white' if piece[0] == 'w' else 'black', piece_rank, self
                        )
                    elif piece[1] == 'F':
                        square.occupying_piece = Fire(
                            (x, y), 'white' if piece[0] == 'w' else 'black', piece_rank, self
                        )
                    elif piece[1] == 'A':
                        square.occupying_piece = Air(
                            (x, y), 'white' if piece[0] == 'w' else 'black', piece_rank, self
                        )
                    elif piece[1] == 'W':
                        square.occupying_piece = Water(
                            (x, y), 'white' if piece[0] == 'w' else 'black', piece_rank, self
                        )
                    
    def handle_click(self, mx, my):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        if self.selected_piece is None:
            if clicked_square.occupying_piece is not None:
                if clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
        elif clicked_square.occupying_piece is not None:
            if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece
    
    
    # checkmate state checker
    def is_in_checkmate(self, color, NPC=None):
        #Returns "in checkmate"
        pieces = [
            i.occupying_piece for i in self.squares if i.occupying_piece is not None
        ]
        home_type = []
        opp_strength = []
        for piece in pieces:
            if piece.color == color:
                home_type.append(piece.notation)
            else:
                opp_strength.append(piece.strength)
            if len(set(home_type)) > 1:
                break
        if len(set(home_type)) == 1:
            if home_type[0] in opp_strength:
                return True

        elif len(home_type) == 0:
            return True
        
        elif NPC != None:
            movable_pieces, possible_moves, opp_pieces = NPC.get_all_moves()
            if (len(possible_moves)==0) | (len(movable_pieces) == 0):
                return True

        return False
    
    def is_in_check(self, color,board_change):
        output = False
        return output
    
    def draw(self, display):
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_valid_moves(self):
                square.highlight = True
        for square in self.squares:
            square.draw(display)