#snakeGame.py
#main game file

import tkinter as tk
import board


if __name__ == "__main__":

    def update(ms_delay):
        root.after(ms_delay, update, ms_delay)


    def center_window(width=600, height=600):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))


    root = tk.Tk()
    root.title('Snake')
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)
    center_window()

    gameBoard = board.Board(grid_size=10, bg="black")
    gameBoard.grid(row=0, column=0, sticky=tk.NSEW)

    root.after(0, update, 1000)
    root.mainloop()
