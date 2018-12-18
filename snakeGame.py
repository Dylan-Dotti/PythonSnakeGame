#snakeGame.py
#main game file

import tkinter as tk
import board
import snake
import food


if __name__ == "__main__":

    def update(ms_delay):
        gameBoard.update()
        root.after(ms_delay, update, ms_delay)

    def center_window(width=600, height=600):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def pressed_w(event):
        gameBoard.handle_key_event('w')

    def pressed_a(event):
        gameBoard.handle_key_event('a')

    def pressed_s(event):
        gameBoard.handle_key_event('s')

    def pressed_d(event):
        gameBoard.handle_key_event('d')

    root = tk.Tk()
    root.title('Snake')
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)

    board_size = 12
    center_window(60 * board_size, 60 * board_size)

    gameBoard = board.Board(board_size, bg="black")
    gameBoard.grid(row=0, column=0, sticky=tk.NSEW)

    spawnPositions = [(5, 5), (5, 6), (5, 7), (5, 8)]
    gameBoard.spawn_snake_at(spawnPositions)

    gameBoard.add_food_at(food.Orange(), 3, 3)
    gameBoard.add_food_at(food.Orange(), 2, 8)
    gameBoard.add_food_at(food.Orange(), 8, 2)

    root.bind("<w>", pressed_w)
    root.bind("<a>", pressed_a)
    root.bind("<s>", pressed_s)
    root.bind("<d>", pressed_d)
    root.bind("<Up>", pressed_w)
    root.bind("<Left>", pressed_a)
    root.bind("<Down>", pressed_s)
    root.bind("<Right>", pressed_d)
    root.after(1000, update, 400)
    root.mainloop()
