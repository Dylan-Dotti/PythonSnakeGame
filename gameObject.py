# python gameObject.py


class GameObject(object):

    def __init__(self, *args, **kwargs):
        super(GameObject, self).__init__(*args, **kwargs)
        self._occupied_tile = None
        self._default_color = "purple"
        self.color = self._default_color

    def occupies_tile(self):
        return self._occupied_tile is not None

    def get_occupied_tile(self):
        return self._occupied_tile

    def move_to_tile(self, tile):
        if self._occupied_tile is not None and \
                self._occupied_tile.get_occupant() == self:
            self._occupied_tile.set_occupant(None)
        self._occupied_tile = tile
        if self._occupied_tile is not None:
            self._occupied_tile.set_occupant(self)

    def get_row(self):
        return self._occupied_tile.get_row()

    def get_column(self):
        return self._occupied_tile.get_column()

    def set_color(self, color):
        if color is None:
            color = self._default_color
        self.color = color
        if self._occupied_tile is not None and \
                self._occupied_tile.get_occupant() == self:
            self._occupied_tile.set_color(color)
