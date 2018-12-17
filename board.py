#board.py

import tkinter as tk
from tkinter import ttk
import tile as tl

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

        for r in range(gridSize):
            for c in range(gridSize):
                newTile = tl.Tile(self, bg="grey")
                tk.Grid.rowconfigure(self, r, weight=1)
                tk.Grid.columnconfigure(self, c, weight=1)
                newTile.grid(row=r, column=c, padx=0.5, pady=0.5, sticky=tk.NSEW)
                self._grid[r].append(newTile)

    def getAt(self, row, col):
        return self._grid[row][col]
