#board.py

import tkinter as tk
from tkinter import ttk
import tile as tl


class Board(tk.Frame):

    def __init__(self, *args, **kwargs):
        #init grid
        if 'grid_size' in kwargs:
            self._grid_size = kwargs['grid_size']
            kwargs.pop('grid_size')
        else:
            self._grid_size = 10
        self._grid = [list() for i in range(self._grid_size)]
        super(Board, self).__init__(*args, **kwargs)

        for r in range(self._grid_size):
            for c in range(self._grid_size):
                new_tile = tl.Tile(r, c, self)
                tk.Grid.rowconfigure(self, r, weight=1)
                tk.Grid.columnconfigure(self, c, weight=1)
                new_tile.grid(row=r, column=c, padx=0.5, pady=0.5, sticky=tk.NSEW)
                self._grid[r].append(new_tile)

    def get_grid_size(self):
        return self._grid_size

    def get_tile_at(self, row, col):
        return self._grid[row][col]
