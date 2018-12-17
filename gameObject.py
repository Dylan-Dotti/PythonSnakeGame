#python gameObject.py


class GameObject(object):

    def __init__(self, *args, **kwargs):
        super(GameObject, self).__init__(*args, **kwargs)
        self._occupied_tile = None
        self._default_color = "purple"
        self._color = default_color

    def get_occupied_tile(self):
        return self._occupied_tile

    def set_occupied_tile(self, tile):
        self._occupied_tile = tile

    def get_row(self):
        return self._occupied_tile.get_row()

    def get_column(self):
        return self._occupied_tile.get_column()

    def set_color(self, color):
        if color is None:
            self._color = self._default_color
        else:
            self._color = color
