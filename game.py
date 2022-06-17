#!/usr/bin/env python3
import numpy as np
import chess 
import chess.pgn

pgn = open("data/November1.pgn")

game = chess.pgn.read_game(pgn)

board = game.board()
i = 0

def move_po(move):
  if(move not in str(board.legal_moves)):
      print("Illegal move")
      return -1
  else:
    board.push_san(move)
    return 0
while (board.is_checkmate()==False):
  for move in game.mainline_moves():
    print(board)
    i+=1
    if(i%2!=0):
      move = input("Enter your move: ")
      while(move_po(move)!=0):
        move = input("Enter your move: ")
    else:
      board.push(move)

