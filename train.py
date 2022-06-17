#!/usr/bin/env python3
import chess
import chess.pgn
import numpy as np
pgn = open("data/November1.pgn")

i = 0
j = 0
games = []
while True:
  game1 = chess.pgn.read_game(pgn)
  if game1== None:
    break
  i = i+1
  for moves in game1.mainline_moves():
    j = j+1
    print(f"parsed {i} games and got {j} moves")
  


  

