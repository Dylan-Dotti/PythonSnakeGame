#tile.py
#tiles for game board

import tkinter as tk


class Tile(tk.Label):

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(*args, **kwargs)