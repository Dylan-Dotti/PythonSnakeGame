# snake.py

import gameObject as go


class Snake(object):

    def __init__(self, board):
        """
        :param board: parent game board
        :param init_positions: list of (r, c) tuples representing initial
        snake part positions
        """
        super(Snake, self).__init__()
        self._parent_board = board
        self._body = []
        self._prev_direction = 'W'
        self._direction = 'W'
        self._grows_remaining = 0

    def __len__(self):
        return len(self._body)

    def update(self):
        if self._parent_board is not None and self.can_move_forward():
            self.move_forward()

    def can_move_forward(self):
        if len(self) == 0:
            return False
        row = self._body[0].get_row()
        col = self._body[0].get_column()
        if self._direction == 'N':
            return self._parent_board.index_in_range(row - 1, col)
        elif self._direction == 'E':
            return self._parent_board.index_in_range(row, col + 1)
        elif self._direction == 'S':
            return self._parent_board.index_in_range(row + 1, col)
        elif self._direction == 'W':
            return self._parent_board.index_in_range(row, col - 1)

    def move_forward(self):
        head = self._body[0]
        head_row = head.get_row()
        head_col = head.get_column()
        prev_tile = self._parent_board.get_tile_at(head_row, head_col)

        # move head
        if self._direction == 'N':
            head.move_to_tile(self._parent_board.get_tile_at(head_row - 1, head_col))
        elif self._direction == 'E':
            head.move_to_tile(self._parent_board.get_tile_at(head_row, head_col + 1))
        elif self._direction == 'S':
            head.move_to_tile(self._parent_board.get_tile_at(head_row + 1, head_col))
        elif self._direction == 'W':
            head.move_to_tile(self._parent_board.get_tile_at(head_row, head_col - 1))

        # move body
        for i in range(1, len(self)):
            part = self._body[i]
            target_tile = prev_tile
            prev_tile = part.get_occupied_tile()
            part.move_to_tile(target_tile)

        # grow if possible
        if self._grows_remaining > 0:
            new_part = Snake.SnakePart()
            new_part.move_to_tile(prev_tile)
            self._body.append(new_part)
            self._grows_remaining -= 1

        # eat food
        food_positions = self._parent_board.get_food_positions()
        for fd in food_positions:
            row, col = food_positions[fd]
            if head.get_row() == row and head.get_column() == col:
                self._grows_remaining += fd.grow_value
                self._parent_board.set_food_eaten(fd)
                break

        self._prev_direction = self._direction

    def can_face_direction(self, direction):
        if self._prev_direction == 'N' and direction == 'S':
            return False
        if self._prev_direction == 'E' and direction == 'W':
            return False
        if self._prev_direction == 'S' and direction == 'N':
            return False
        if self._prev_direction == 'W' and direction == 'E':
            return False
        return True

    def set_direction(self, direction):
        if self.can_face_direction(direction):
            self._direction = direction

    def get_occupied_tiles(self):
        occ_tiles = []
        for part in self._body:
            if part.occupies_tile():
                occ_tiles.append(part.get_occupied_tile())
        return occ_tiles

    def occupies_position(self, row, col):
        for part in self._body:
            if part.get_row() == row and part.get_column() == col:
                return True
        return False

    def spawn_at(self, positions):
        self.remove_from_board()
        self._body = []
        for row, col in positions:
            new_part = Snake.SnakePart()
            spawn_tile = self._parent_board.get_tile_at(row, col)
            new_part.move_to_tile(spawn_tile)
            self._body.append(new_part)

    def remove_from_board(self):
        for part in self._body:
            part.move_to_tile(None)

    def eat_food(self, food):
        pass

    class SnakePart(go.GameObject):

        def __init__(self, *args, **kwargs):
            super(Snake.SnakePart, self).__init__(*args, **kwargs)
            self._default_color = "green"
            self.set_color(self._default_color)
