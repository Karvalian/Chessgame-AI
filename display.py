#!/usr/bin/python3
import chess
import chess.svg
from IPython.display import SVG

class Display():
  def display(board):
    SVG(str(board).encode())
