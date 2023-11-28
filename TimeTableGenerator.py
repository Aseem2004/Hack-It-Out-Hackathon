from tkinter import *

def one():
    global main
 
    main=Tk()
    main.title("Time Table Generator")
    main.geometry('900x600')
    main.minsize(900,600)
    main.maxsize(900,600)
    global name
    global password
    name=StringVar()
    password=StringVar()
   
    def time():
        global TT
        TT=Tk()
        TT.title("Time Table Generator")
        global thsub
        global ansub
        global labsub
        thsub=IntVar()
        ansub=IntVar()
        labsub=IntVar()
        TT.geometry('950x700')
        TT.minsize(950,700)
        TT.maxsize(950,700)