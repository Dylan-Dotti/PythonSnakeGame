#snake.py

import gameObject as go


class Snake(object):

    class SnakePart(go.GameObject):

        def __init__(self, *args, **kwargs):
            super(SnakePart, self, *args, **kwargs)
            self._default_color = "green"

    def __init__(self, *args, **kwargs):
        super(Snake, self, *args, **kwargs)
