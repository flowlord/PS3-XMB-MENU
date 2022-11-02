#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#LKPOS23
from tkinter import*
MainActivity = Tk()
MainActivity.title("LKPOS23")
MainActivity.configure(bg="#fff")

#MainActivity.iconbitmap('logo_compt.ico')

selection = Frame(MainActivity, bg="#46b9eb", width=600, height=80, relief=FLAT)
selection.pack_propagate(False)
selection.pack()


CATEGORIE1 = Label(selection, text="CATEGORIE 1", bg="#46b9eb", fg="white", font=(None, 31))
CATEGORIE1.pack(pady=25, padx=25)


item_text_one = Label(MainActivity,  text="ITEM 1", bg="#fff",fg="black", font=(None, 30))
item_text_one.pack(pady=25, padx=25)
item_text_two = Label(MainActivity,  text="ITEM 2",bg="#fff" ,fg="black", font=(None, 30))
item_text_two.pack(pady=25, padx=25)


def clavier(event):
    global coords
    touche = event.keysym
    if touche == "Down":

        CATEGORIE1.config(bg="#fff", fg="black", font=(None, 30))
        CATEGORIE1.pack(pady=25, padx=25)
        item_text_one.config(selection, bg="#46b9eb", fg="white", font=(None, 31))
        item_text_one.pack(pady=25, padx=25)


CATEGORIE1.focus_set()
CATEGORIE1.bind("<Down>", clavier)


MainActivity.mainloop()

