import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

import fileTransfer_main
import fileTransfer_gui

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

#=====================================================================================================

#   Grabs the the chosen file path and places it in the Entry
def callback(self, num):
    name = fd.askdirectory()
    path = 'self.txt_bar{}.insert(END, name)'.format(num)
    delpath = 'self.txt_bar{}.delete(0, END)'.format(num)
    #   If there are no text, will add the file path in the entry
    if not path:
        exec(path)
    #   If there are text, will delete then enter new path
    else:
        exec(delpath)
        exec(path)
        

        
    

    
    
