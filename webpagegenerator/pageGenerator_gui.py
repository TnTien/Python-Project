import tkinter as tk
from tkinter import *

import pageGenerator_main
import pageGenerator_func
import pageGenerator

def load_gui(self):

    #   Displays text above the text box
    self.lbl_message = tk.Label(self.master, text="Enter message to display:")
    self.lbl_message.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    #   Text box to enter new text to update the body of the HTML
    self.msgEntry = tk.Text(self.master, height=8, width=30)
    self.msgEntry.grid(row=1, column=0, columnspan=2, padx=(27,5), pady=(5,5), sticky=N+W)
    #   This will get the text from the textbox and update the HTML page and load the page
    self.btn_check = tk.Button(self.master,width=12, text='Update...', command=lambda: pageGenerator_func.take_input(self))
    self.btn_check.grid(row=3, column=0,padx=(27,0), pady=(5,5), sticky=W)
    #   This will clear the textbox
    self.btn_clear = tk.Button(self.master, width=12, text="Clear", command=lambda: pageGenerator_func.clear(self))
    self.btn_clear.grid(row=4, column=0,padx=(27,0), pady=(5,5), sticky=W)
    #   Closes the program
    self.btn_close = tk.Button(self.master,width=12, text='Close Program', command=lambda: pageGenerator_func.ask_quit(self))
    self.btn_close.grid(row=3, column=1,padx=(0,1), pady=(5,5),sticky=E)

if __name__ == "__main__":
    pass
