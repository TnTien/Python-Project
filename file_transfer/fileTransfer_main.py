import tkinter as tk
from tkinter import *

import fileTransfer_gui
import fileTransfer_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #   Program Window
        self.master = master
        self.master.minsize(475, 175)
        self.master.maxsize(475, 175)

        #   Will Center the window to the screen
        fileTransfer_func.center_window(self, 475, 175)

        #   Closes program when the 'X' is clicked
        self.master.protocol("WM_DELETE_WINDOW", lambda: fileTransfer_func.ask_quit(self))
        arg = self.master

        #   Text that displays on the top of the program
        self.master.title("File Transfer")

        #   Loads the GUI
        fileTransfer_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
