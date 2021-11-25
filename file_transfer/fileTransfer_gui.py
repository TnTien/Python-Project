import tkinter as tk
from tkinter import *

import fileTransfer_main
import fileTransfer_func
import fileTransfer

def load_gui(self):
    self.lbl = tk.Label(self.master, text='Please choose the folder you woud like checked and where to move them.')
    self.lbl.grid(row=0, column=0, columnspan=5, padx=(15,25), pady=(15,5), sticky=W)
    
    self.btn_browse1 = tk.Button(self.master,width=12, text='Source...', command=lambda: fileTransfer_func.callback(self, 1))
    self.btn_browse1.grid(row=1, column=0,padx=(15,25),pady=(5,5),sticky=S)
    self.btn_browse2 = tk.Button(self.master,width=12, text='Destination...', command=lambda: fileTransfer_func.callback(self, 2))
    self.btn_browse2.grid(row=2, column=0,padx=(15,25), pady=(5,5),sticky=S)
    self.btn_transfer = tk.Button(self.master,width=12, height=2, text='Transfer files...', command=lambda: fileTransfer.transfer(self))
    self.btn_transfer.grid(row=3, column=0, rowspan=3,padx=(15,25), pady=(5,5), sticky=S)

    self.btn_close = tk.Button(self.master,width=12, height=2, text='Close Program', command=lambda: fileTransfer_func.ask_quit(self))
    self.btn_close.grid(row=3, column=4,padx=(0,1), rowspan=3, pady=(5,5),sticky=S+E)

    self.txt_bar1 = tk.Entry(self.master,width=52, text='')
    self.txt_bar1.grid(row=1, column=1,padx=(0,1), columnspan=4, pady=(5,5),sticky=N)
    self.txt_bar2 = tk.Entry(self.master,width=52, text='')
    self.txt_bar2.grid(row=2, column=1,padx=(0,1), columnspan=4, pady=(5,5),sticky=N)

    

if __name__ == "__main__":
    pass

    
