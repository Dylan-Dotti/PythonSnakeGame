#tile.py
#tiles for game board

import tkinter as tk


class Tile(tk.Label):

    def __init__(self, row, col, *args, **kwargs):
        super(Tile, self).__init__(*args, **kwargs)
        if 'bg' in kwargs:
            self._default_color = kwargs['bg']
        else:
            self._default_color = "grey"
            self.set_color(self._default_color)
        self._row = row
        self._col = col
        self._occupant = None

    def get_row(self):
        return self._row

    def get_column(self):
        return self._col

    def is_occupied(self):
        return self._occupant is not None

    def get_occupant(self):
        return self._occupant

    def set_occupant(self, game_obj):
        self._occupant = game_obj
        if game_obj is None:
            self.set_color(None)
        else:
            self.set_color(game_obj.color)

    def set_color(self, color):
        if color is None:
            color = self._default_color
        self.config(bg=color)
