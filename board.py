#board.py

import tkinter as tk
from tkinter import ttk

class Board(tk.Frame):

    def __init__(self, *args, **kwargs):
        #init grid
        if kwargs['gridSize']:
            gridSize = kwargs['gridSize']
            kwargs.pop('gridSize')
        else:
            gridSize = 10
        self._grid = [list() for i in range(gridSize)]
        super(Board, self).__init__(*args, **kwargs)

        for r in range(len(gridSize)):
            for c in range(len(gridSize)):
                pass

    def getAt(self, row, col):
        return self._grid[row][col]
