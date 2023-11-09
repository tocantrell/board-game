import pygame
import time

from data.classes.Board import Board
from data.classes.NPC import NPC

run_npc = True

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
npc_b = NPC(board,'black')
npc_w = NPC(board,'white')

def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.update()


if __name__ == '__main__':
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			# Quit the game if the user presses the close button
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: 
       			# If the mouse is clicked
				if event.button == 1:
					board.handle_click(mx, my)
		if board.is_in_checkmate('black'): # If black is in checkmate
			print('White wins!')
			print('Turns: ' + str(npc_b.move_count))
			running = False
		elif board.is_in_checkmate('white'): # If white is in checkmate
			print('Black wins!')
			print('Turns: ' + str(npc_w.move_count))
			running = False
		elif run_npc:
			if board.turn == 'black':
				time.sleep(0.5)
				movable_pieces, possible_moves,  opp_pieces = npc_b.get_all_moves()
				#npc.move_random(movable_pieces, possible_moves)
				npc_b.move_greedy(movable_pieces, possible_moves, opp_pieces)
				
			#elif board.turn == 'white':
			#	movable_pieces, possible_moves,  opp_pieces = npc_w.get_all_moves()
			#	npc_w.move_random(movable_pieces, possible_moves)
				#npc.move_greedy(movable_pieces, possible_moves, opp_pieces)
			#	time.sleep(1)
		# Draw the board
		draw(screen)