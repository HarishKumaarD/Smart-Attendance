from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Student Details")

        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=40)

        img_top=Image.open(r"images\dev.jpg")
        img_top=img_top.resize((1300,650),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1300,height=650)


        # frame

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=880,y=50,width=380,height=500)


        # Developer Info

        
        Developer_lbl=Label(main_frame,text="1.Name:-abc",font=("times new roman",20,"bold"),bg="white",fg="green")
        Developer_lbl.place(x=5,y=0)

        Developer_lbl=Label(main_frame,text="2.Name:-abc",font=("times new roman",20,"bold"),bg="white",fg="green")
        Developer_lbl.place(x=5,y=35)

        Developer_lbl=Label(main_frame,text="2.Name:-abc",font=("times new roman",20,"bold"),bg="white",fg="green")
        Developer_lbl.place(x=5,y=70)


        img_top1=Image.open(r"images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img_top1=img_top1.resize((380,400),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=200,width=380,height=400)
        




if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()