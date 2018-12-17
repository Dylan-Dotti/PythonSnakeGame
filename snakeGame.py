#snakeGame.py
#main game file

import tkinter as tk
import board


def update(ms_delay):
    root.after(ms_delay, update, ms_delay)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Snake')
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)
    root.geometry('600x600')

    gameBoard = board.Board(grid_size=10, bg="black")
    gameBoard.grid(row=0, column=0, sticky=tk.NSEW)

    root.after(0, update, 1000)
    root.mainloop()
