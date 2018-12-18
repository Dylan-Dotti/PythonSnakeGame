#board.py

import tkinter as tk
import tile
import snake


class Board(tk.Frame):

    def __init__(self, grid_size=10, *args, **kwargs):
        #init grid
        super(Board, self).__init__(*args, **kwargs)
        self._grid_size = grid_size
        self._grid = [list() for i in range(self._grid_size)]

        for r in range(self._grid_size):
            for c in range(self._grid_size):
                new_tile = tile.Tile(r, c, self)
                tk.Grid.rowconfigure(self, r, weight=1)
                tk.Grid.columnconfigure(self, c, weight=1)
                new_tile.grid(row=r, column=c, padx=0.5, pady=0.5, sticky=tk.NSEW)
                self._grid[r].append(new_tile)

        self.food_positions = {}
        self.player_snake = None

    def update(self):
        if self.player_snake is not None:
            self.player_snake.update()

    def handle_key_event(self, key):
        if key == 'w':
            self.player_snake.set_direction('N')
        if key == 'a':
            self.player_snake.set_direction('W')
        if key == 's':
            self.player_snake.set_direction('S')
        if key == 'd':
            self.player_snake.set_direction('E')

    def get_grid_size(self):
        return self._grid_size

    def index_in_range(self, row, col):
        return 0 <= row < self._grid_size and 0 <= col < self._grid_size

    def get_tile_at(self, row, col):
        return self._grid[row][col]

    def spawn_snake_at(self, positions):
        """
        :param positions: list of (row, col) tuples
        """
        if self.player_snake is not None:
            self.player_snake.remove_from_board()
        self.player_snake = snake.Snake(self)
        self.player_snake.spawn_at(positions)

    def add_food_at(self, food, row, col):
        spawn_tile = self.get_tile_at(row, col)
        if spawn_tile in self.player_snake.get_occupied_tiles():
            raise ValueError('snake occupies that position')
        self.food_positions[food] = (row, col)

    def remove_food(self, food):
        if food in self.food_positions:
            food.move_to_tile(None)
            self.food_positions.pop(food)

    def has_food_at(self, row, col):
        for r, c in self.food_positions.values():
            if r == row and c == col:
                return True
        return False

    def get_food_positions(self):
        return self.food_positions
