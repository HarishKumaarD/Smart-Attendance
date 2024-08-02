from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Student Details")
        # ======== Variables ==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # first image
        img=Image.open(r"images\student2.jpg")
        img=img.resize((640,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=640,height=150)

        # second image
        img1=Image.open(r"images\student3.jpg")
        img1=img1.resize((640,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=640,y=0,width=640,height=150)

        title_lbl=Label(self.root,text="ATTENDANCE MANAGMENT SYSYTEM",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=150,width=1300,height=40)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=0,y=192,width=1280,height=480)


        # left frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=625,height=450)

        img_left=Image.open(r"E:\Face Recognition Project\images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((625,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=605,height=120)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=125,width=605,height=300)


        
        # Label Entry Attendance Id
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Label Entry Roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Label Entry Name 
        Name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
       
        # Label Entry Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Label Entry time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Label Entry Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Attendance
        Attendance_label=Label(left_inside_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        self.Attendance_combo=ttk.Combobox(left_inside_frame,width=16,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.Attendance_combo["values"]=("Select Status","Present","Absent")
        self.Attendance_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        self.Attendance_combo.current(0)


        # Button frame
         
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=600,height=34)

        import_btn=Button(btn_frame,text="Import Csv",width=15,command=self.import_csv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export Csv",width=15,command=self.export_csv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)
        
        Update_btn=Button(btn_frame,text="Update",width=16,command=self.get_cursor,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=645,y=0,width=622,height=450)

        # Scroll Table
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=605,height=420)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("Id","Roll","Name","Department","Time","Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll",text="Roll No.")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")

        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.column("Id",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)        

# =================== Fetching the data ==============
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


# ========= import csv=================
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

# =============== export csv==================

    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"succesfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    # uodate function ==============

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])
    
    # reset function ==============

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()