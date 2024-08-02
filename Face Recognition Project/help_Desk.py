from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class HelpDesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Student Details")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1550,height=40)



        # 1st Image
        img_top=Image.open(r"images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1550,750),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1550,height=750)


        help_desk_lbl=Label(f_lbl,text="Email:-abc@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        help_desk_lbl.place(x=600,y=170)




if __name__ =="__main__":
    root=Tk()
    obj=HelpDesk(root)
    root.mainloop()