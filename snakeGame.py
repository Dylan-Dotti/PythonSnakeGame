#snakeGame.py
#main game file

import tkinter as tk
from tkinter import ttk
import board


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Hello Tkinter')
    root.geometry('800x600')

    gameBoard = board.Board(gridSize=10)

    root.mainloop()
