from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Student Details")

        # ================ Variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

# first image
        img=Image.open(r"D:\Face Recognition Project\images\student.jpg")
        img=img.resize((430,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=110)

        # second image
        img1=Image.open(r"D:\Face Recognition Project\images\student2.jpg")
        img1=img1.resize((430,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=430,y=0,width=430,height=110)

        # third image
        img2=Image.open(r"D:\Face Recognition Project\images\student3.jpg")
        img2=img2.resize((430,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=860,y=0,width=430,height=110)

        # Background image
        img3=Image.open(r"D:\Face Recognition Project\images\bgimg.jpg")
        img3=img3.resize((1300,570),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=110,width=1300,height=570)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=40)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=14,y=48,width=1250,height=480)

        # left frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=610,height=460)


        img_left=Image.open(r"D:\Face Recognition Project\images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((600,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=587,height=90)

        # Current Course Frame

        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",10,"bold"))
        current_course_frame.place(x=10,y=90,width=587,height=80)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Mechanical","Electrical","Electronics","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)
        # Program
        course_label=Label(current_course_frame,text="Program",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","BE","TE","SE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)
        
        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semeter",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)
        
        # class Student Details
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Details",font=("times new roman",10,"bold"))
        class_student_frame.place(x=10,y=173,width=587,height=255)

        # StudentIB label

        studentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name label

        student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",10,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",10,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # CLass Devision label

        class_devison_label=Label(class_student_frame,text="Class Devision:",font=("times new roman",10,"bold"),bg="white")
        class_devison_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        devision_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=13,font=("times new roman",10,"bold"),state="readonly")
        devision_combo["values"]=("Select Devision","A","B","C")
        devision_combo.current(0)
        devision_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll No. label

        roll_no_label=Label(class_student_frame,text="Roll_No:",font=("times new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender label

        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",10,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=13,font=("times new roman",10,"bold"),state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB label

        DOB_label=Label(class_student_frame,text="DOB:",font=("times new roman",10,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",10,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        # email label

        email_label=Label(class_student_frame,text="Email:",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        # phone label

        phone_no_label=Label(class_student_frame,text="Phone_No:",font=("times new roman",10,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",10,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        # address label

        address_label=Label(class_student_frame,text="Address:",font=("times new roman",10,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        # teacher label

        teacher_name_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",10,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=5,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",10,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Samples",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Samples",value="No")
        radiobtn2.grid(row=6,column=1)
        
        # button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=175,width=583,height=34)

        save_btn=Button(btn_frame,text="Save",width=15,command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=15,command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",width=15,command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=204,width=583,height=30)


        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=31,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        # Right frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=630,y=10,width=610,height=460)

        img_right=Image.open(r"D:\Face Recognition Project\images\student.jpg")
        img_right=img_right.resize((600,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=587,height=90)

        # ========== Search System ============

        Search_system_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",10,"bold"))
        Search_system_frame.place(x=10,y=92,width=587,height=70)

        search_label=Label(Search_system_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)


        search_combo=ttk.Combobox(Search_system_frame,font=("times new roman",10,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll No.","phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        search_entry=ttk.Entry(Search_system_frame,width=15,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)


        search_btn=Button(Search_system_frame,text="Search",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)
        
        showAll_btn=Button(Search_system_frame,text="Show All",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)

        # ==============Table frame ================
        
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=175,width=587,height=255)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Devision")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="photoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # =============== Function Declaration =============================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="ROOT",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


# ================= fetch the data================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="ROOT",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# =================== Get Cursor ===================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

# ======== Update function =====================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="ROOT",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,year=%s,Semester=%s,StudentName=%s,Division=%s,RollNo=%s,Gender=%s,DateOfBirth=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,photoSampleStatus=%s where StudentID=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),    
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student details succesfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# =========== delete button ==================


    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to Delete this Student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="ROOT",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

# ========== reset function================

    def reset_data(self):
        self.var_dep.set("Select department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

# ========= Generting the data set and taking the Photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="ROOT",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,year=%s,Semester=%s,StudentName=%s,Division=%s,RollNo=%s,Gender=%s,DateOfBirth=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,photoSampleStatus=%s where StudentID=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),    
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

#  =========== load predifined data on face frontals from openCV =============
                net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')

                def face_cropped(img):
                    # Resize the image for the model
                    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104, 177, 123))

                    # Pass the blob through the network to detect faces
                    net.setInput(blob)
                    detections = net.forward()

                    for i in range(detections.shape[2]):
                        confidence = detections[0, 0, i, 2]

                        if confidence > 0.5:  # Adjust confidence threshold as needed
                            box = detections[0, 0, i, 3:7] * np.array([img.shape[1], img.shape[0], img.shape[1], img.shape[0]])
                            (x, y, w, h) = box.astype(int)

                            # Crop and return the detected face
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (600, 600))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 30:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  



        
if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()