#food.py

import gameObject as go


class Food(go.GameObject):

    def __init__(self, score_value=0, grow_value=0, *args, **kwargs):
        super(Food, self).__init__(*args, **kwargs)
        self.score_value = score_value
        self.grow_value = grow_value

    def get_score_value(self):
        return self.score_value

    def get_grow_value(self):
        return self.grow_value


class Orange(Food):

    def __init__(self, *args, **kwargs):
        super(Orange, self).__init__(5, 2, *args, **kwargs)
        self._default_color = "orange"
        self.set_color(self._default_color)
