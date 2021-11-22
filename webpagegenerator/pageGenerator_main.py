import tkinter as tk
from tkinter import *

import pageGenerator_gui
import pageGenerator_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        #   Size of window of the program
        self.master.minsize(400, 325)
        self.master.maxsize(400, 325)

        #   Will center the window when program first opens
        pageGenerator_func.center_window(self, 400, 325)

        #   Message box to confirm to quit program when 'X' is clicked
        self.master.protocol("WM_DELETE_WINDOW", lambda: pageGenerator_func.ask_quit(self))
        arg = self.master

        #   Title that wil display on top of window
        self.master.title("Web Page Generator")

        # Loads the GUI
        pageGenerator_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
