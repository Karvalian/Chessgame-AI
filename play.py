#!/usr/bin/env python3
import chess
import random
import chess.svg
board = chess.Board()


def move(mv):
  if(mv in str(board.legal_moves)):
    board.push_san(mv)
    return 0
  else:
    print("Illegal move")
    return -1
#i=0
while(board.is_checkmate()!=True):
  print(board)
  print("\n")
  #i+=1
  if(board.turn==False):
    print("Bot's move")
    mv = random.choice(list(board.legal_moves))
    board.push_san(str(mv))
  else:
    mv = input("Your move : ")
    while(move(mv)!=0):
      mv = input("Your move : ")
    
