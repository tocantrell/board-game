import pygame
import time
import pandas as pd


from data.classes.Board import Board
from data.classes.NPC import NPC

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
npc_b = NPC(board,'black')
npc_w = NPC(board,'white')

#def draw(display):
#	display.fill('white')
#	board.draw(display)
#	pygame.display.update()

def get_stats(board,npc_win,npc_lose):
	win_piece = npc_win.last_move_type
	win_rank = npc_win.last_move_rank
	win_color = npc_win.npc_color
	win_pieces = npc_win.get_piece_count()
	lose_pieces = npc_lose.get_piece_count()
	move_count = npc_win.move_count
	df = pd.DataFrame({'moves':[move_count],
					'winning_color':[win_color],
					'winning_piece':[win_piece],
					'winning_rank':[win_rank],
					'winner_num_pieces':[win_pieces],
					'loser_num_pieces':[lose_pieces]})
	return df



if __name__ == '__main__':
	game_count = 0
	games_to_do = 1000
	total_count = 0
	total_count_limit = 5000
	df = pd.DataFrame()
	running = True
	while running:
		if board.is_in_checkmate('black', npc_b): # If black is in checkmate
			#running = False
			df_mid = get_stats(board,npc_w,npc_b)
			df = pd.concat([df,df_mid])
			game_count+=1
			print(game_count)
			if game_count >=games_to_do:
				running = False
			else:
				del board, npc_b, npc_w
				board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
				npc_b = NPC(board,'black')
				npc_w = NPC(board,'white')
		elif board.is_in_checkmate('white', npc_w): # If white is in checkmate
			#running = False
			df_mid = get_stats(board,npc_b,npc_w)
			df = pd.concat([df,df_mid])
			game_count+=1
			print(game_count)
			if game_count >=games_to_do:
				running = False
			else:
				del board, npc_b, npc_w
				board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
				npc_b = NPC(board,'black')
				npc_w = NPC(board,'white')
		elif board.turn == 'black':
			movable_pieces, possible_moves,  opp_pieces = npc_b.get_all_moves()
			#npc.move_random(movable_pieces, possible_moves)
			npc_b.move_greedy(movable_pieces, possible_moves, opp_pieces)
			#time.sleep(1)
		elif board.turn == 'white':
			movable_pieces, possible_moves,  opp_pieces = npc_w.get_all_moves()
		#	npc_w.move_random(movable_pieces, possible_moves)
			npc_w.move_greedy(movable_pieces, possible_moves, opp_pieces)
		#	time.sleep(1)
		if game_count % 100 == 0:
			df.to_csv('random_stats_mid.csv',index=False)
		#total_count+=1
		#print(total_count)
		#if total_count > total_count_limit:
		#	running=False
			
		
	print(game_count)
	df.to_csv('random_stats.csv',index=False)
		
