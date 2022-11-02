#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
LKPOS23
02/11/2022
from: https://openclassrooms.com/forum/sujet/python-3-x-naviguer-dans-un-menu-avec-les-touche
"""

from tkinter import*

BC = "#000"

root = Tk()
root.title("LKPOS23")
root.configure(bg=BC)

t_width = 25
t_height = 10
t_pady,t_padx = 5,5

a_color = "#a8f7a8"
b_color = "#ff3f42"
c_color = "#593f5e"

"""
SELECTOR = Frame(root, highlightbackground = "#ffff00", 
                         highlightthickness = 2, bd=0,background=BC)
SELECTOR.pack()

"""

ta = Label(root,text="A",width = t_width,height=t_height,background=a_color,highlightbackground = "#ffff00",
highlightthickness = 2,bd=0)
ta.pack(pady=t_pady, padx=t_padx)

tb = Label(root,text="B",width = t_width,height=t_height,background=b_color,highlightbackground = "#ffff00",
highlightthickness = 0,bd=0)
tb.pack(pady=t_pady, padx=t_padx)

tc = Label(root,text="C",width = t_width,height=t_height,background=c_color,highlightbackground = "#ffff00",
highlightthickness = 0,bd=0)
tc.pack(pady=t_pady, padx=t_padx)

def write_tmp_file(d):
    active_tuil = open("user.tmp","w").write(d)


def switch(event):

    touche = event.keysym
    if touche == "Down":

        active_tuil = open("user.tmp","r").read()

        if active_tuil == "ta":
            ta.config(highlightthickness = 0)
            tb.config(highlightthickness = 2)
            write_tmp_file("tb")
        
        elif active_tuil == "tb":
            tb.config(highlightthickness = 0)
            tc.config(highlightthickness = 2)
            write_tmp_file("tc")
        
        elif active_tuil == "tc":
            tc.config(highlightthickness = 0)
            ta.config(highlightthickness = 2)
            write_tmp_file("ta")



root.focus_set()
root.bind("<Down>", switch)


root.mainloop()














