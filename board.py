# board.py

import tkinter as tk
import random
import tile
import snake


class Board(tk.Frame):

    def __init__(self, rows=10, cols=10, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)
        self.num_rows = rows
        self.num_columns = cols
        self._grid = [list() for i in range(self.num_rows)]

        for r in range(self.num_rows):
            for c in range(self.num_columns):
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
        return 0 <= row < self.num_rows and 0 <= col < self.num_columns

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

    def get_food_positions(self):
        """
        :return: dict of food to (row, col) position
        """
        return self.food_positions

    def add_food_at(self, food, row, col):
        spawn_tile = self.get_tile_at(row, col)
        if spawn_tile in self.player_snake.get_occupied_tiles():
            raise ValueError('snake occupies (' + row + ', ' + col + ')')
        if self.has_food_at(row, col):
            raise ValueError('food already occupies (' + row + ', ' + col + ')')
        self.food_positions[food] = (row, col)
        food.move_to_tile(spawn_tile)

    def remove_food(self, food):
        if food in self.food_positions:
            food.move_to_tile(None)
            self.food_positions.pop(food)

    def has_food_at(self, row, col):
        for r, c in self.food_positions.values():
            if r == row and c == col:
                return True
        return False

    def set_food_eaten(self, food):
        self.spawn_food_random(food)

    def spawn_food_random(self, food):
        # add check for full board
        self.remove_food(food)
        while True:
            new_row = random.randint(0, self.num_rows - 1)
            new_col = random.randint(0, self.num_columns - 1)
            if not self.player_snake.occupies_position(new_row, new_col) and \
                    not self.has_food_at(new_row, new_col):
                break
        self.add_food_at(food, new_row, new_col)
