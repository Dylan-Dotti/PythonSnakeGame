#board.py

import tkinter as tk
import tile


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
                new_tile = tile.Tile(r, c, self)
                tk.Grid.rowconfigure(self, r, weight=1)
                tk.Grid.columnconfigure(self, c, weight=1)
                new_tile.grid(row=r, column=c, padx=0.5, pady=0.5, sticky=tk.NSEW)
                self._grid[r].append(new_tile)

        self.food = []

    def get_grid_size(self):
        return self._grid_size

    def index_in_range(self, row, col):
        return 0 <= row < self._grid_size and 0 <= col < self._grid_size

    def get_tile_at(self, row, col):
        return self._grid[row][col]

    def get_food(self):
        pass
