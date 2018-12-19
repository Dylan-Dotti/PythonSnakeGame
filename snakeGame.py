# snakeGame.py
# main game file

import tkinter as tk
import board
import snake
import food
import time


if __name__ == "__main__":

    class SnakeGame(object):

        def __init__(self):
            super(SnakeGame, self).__init__()

            self.root = tk.Tk()
            self.root.title('Snake')
            tk.Grid.rowconfigure(self.root, 0, weight=1)
            tk.Grid.columnconfigure(self.root, 0, weight=1)

            self.game_board = None
            self.spawn_game_board()

            self.root.bind("<w>", self.pressed_w)
            self.root.bind("<a>", self.pressed_a)
            self.root.bind("<s>", self.pressed_s)
            self.root.bind("<d>", self.pressed_d)
            self.root.bind("<Up>", self.pressed_w)
            self.root.bind("<Left>", self.pressed_a)
            self.root.bind("<Down>", self.pressed_s)
            self.root.bind("<Right>", self.pressed_d)
            self.root.after(1000, self.update, 300)
            self.root.mainloop()

        def update(self, ms_delay):
            self.game_board.update()
            self.root.after(ms_delay, self.update, ms_delay)

        def center_window(self, width=600, height=600):
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

        def pressed_w(self, event):
            self.game_board.handle_key_event('w')

        def pressed_a(self, event):
            self.game_board.handle_key_event('a')

        def pressed_s(self, event):
            self.game_board.handle_key_event('s')

        def pressed_d(self, event):
            self.game_board.handle_key_event('d')

        def on_player_death(self):
            print('player death')
            time.sleep(2)
            self.game_board.destroy()
            self.spawn_game_board()

        def spawn_game_board(self):
            num_rows = 12
            num_cols = 20
            self.center_window(60 * num_cols, 60 * num_rows)

            gb = board.Board(num_rows, num_cols, self.on_player_death, self.root, bg="black")
            gb.grid(row=0, column=0, sticky=tk.NSEW)

            spawn_positions = [(5, 5), (5, 6), (5, 7), (5, 8)]
            gb.spawn_snake_at(spawn_positions)

            gb.add_food_at(food.Orange(), 3, 3)
            gb.add_food_at(food.Orange(), 2, 8)
            gb.add_food_at(food.Orange(), 8, 2)

            self.game_board = gb

    main_game = SnakeGame()
