import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import pageGenerator_main
import pageGenerator_gui
import pageGenerator

def center_window(self, w, h):  #   Pass in the tkinter frame (master) reference and the w and h
        #   get user's screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        #   calculate x and y coordinates to paint the app centered on the user's screen
        x = int((screen_width/2) - (w/2))
        y = int((screen_height/2) - (h/2))
        centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        return centerGeo

#   Catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

#========================================================================

#   Grabs the text and update HTML
def take_input(self):
    #   Stores the text in the textbox
    take = self.msgEntry.get("1.0", END)
    #   Calls the function from pageGenerator and updates the text
    pageGenerator.createPage(self, take)
    print(take)

#   Clears the text box
def clear(self):
    clear = self.msgEntry.delete("1.0", END)

    







if __name__ == "__main__":
    pass
