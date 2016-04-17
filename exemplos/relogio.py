from tkinter import Label
from time import strftime

rel = Label()
rel['font'] = 'Verdana 80 bold'
rel['text'] = strftime('%H:%M:%S')
rel.pack()

def tictac():
    rel['text'] = strftime('%H:%M:%S')
    rel.after(100, tictac)

tictac()

rel.mainloop()
