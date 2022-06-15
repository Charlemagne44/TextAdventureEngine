from tkinter.constants import LEFT, W
from Model import *
from View import *
import tkinter as tk

class Controller:

    def __init__(self):
        window = tk.Tk()
        #greeting = tk.Label(text="Testing, testing")
        #greeting.pack()
        frm_console = tk.Frame(
            relief=tk.RIDGE,
            master=window,
            background='black'
        )
        frm_input = tk.Frame(
            relief=tk.SUNKEN,
            #borderwidth=5,
            master=window,
            background='black'
        )
        btn_enter = tk.Button(
            text='enter',
            bg='black',
            fg='white',
            master=frm_input,
        )
        ent_input = tk.Entry(
            fg='white',
            bg='black',
            master=frm_input,
            #command=getInput
        )
        lbl_console =  tk.Label(
            master=frm_console,
            text='Change later',
            bg='black',
            fg='white',
            anchor=W
        )

        btn_enter.pack(side=tk.RIGHT)
        ent_input.pack(side=tk.LEFT)
        lbl_console.pack()

        frm_console.pack(fill=tk.X,anchor=W)
        frm_input.pack(fill=tk.X)
        
        window.mainloop()
    

#    if __name__ == "__main__":
#        main(0)