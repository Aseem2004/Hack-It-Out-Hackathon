from tkinter import *

def one():
    global main
 
    main=Tk()
    main.title("Time Table Generator")
    main.geometry('800x500')
    main.minsize(800,500)
    main.maxsize(800,500)
    global name
    global password
    name=StringVar()
    password=StringVar()