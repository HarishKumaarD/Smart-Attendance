from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from datetime import datetime

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Student Details")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=90, y=0, width=1300, height=40)

        img_top = Image.open("D:\\Face Recognition Project\\images\\face_detector1.jpg")
        img_top = img_top.resize((775, 750), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=775, height=750)

        img_bottom = Image.open(r"D:\Face Recognition Project\images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((775, 750), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_1 = Label(self.root, image=self.photoimg_bottom)
        f_lbl_1.place(x=775, y=40, width=775, height=750)

        b1_1 = Button(f_lbl_1, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=300, y=660, width=185, height=35)

    def mark_attendance(self, student_id, roll_no, student_name, department):
        with open("Attendance.csv", "a", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if student_id not in name_list and roll_no not in name_list and student_name not in name_list and department not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{student_id},{roll_no},{student_name},{department},{dtString},{d1},Present\n")


    def draw_boundary(self, img, startX, startY, endX, endY, color, student_id, roll_no, student_name, department):
        cv2.rectangle(img, (startX, startY), (endX, endY), color, 2)
        cv2.putText(img, f"ID: {student_id}", (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.putText(img, f"Roll: {roll_no}", (startX, startY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.putText(img, f"Name: {student_name}", (startX, startY + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.putText(img, f"Department: {department}", (startX, startY + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.rectangle(img, (startX, startY - 15), (endX, endY + 100), color, 2)


    def recognize(self, img):
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        self.face_net.setInput(blob)
        detections = self.face_net.forward()

        (h, w) = img.shape[:2]

        startX, startY, endX, endY = 0, 0, 0, 0

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype(int)

                face = img[startY:endY, startX:endX]
                face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convert the face to grayscale

                id, predict = self.clf.predict(face_gray)  # Pass the grayscale face to predict

                conn = mysql.connector.connect(host="localhost", user="root", password="ROOT", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute(f"Select StudentName from student where StudentID = {id}")
                student_name = "+".join(map(str, my_cursor.fetchone()))

                my_cursor.execute(f"Select RollNo from student where StudentID = {id}")
                roll_no = "+".join(map(str, my_cursor.fetchone()))

                my_cursor.execute(f"Select Department from student where StudentID = {id}")
                department = "+".join(map(str, my_cursor.fetchone()))

                my_cursor.execute(f"Select StudentID from student where StudentID = {id}")
                student_id = "+".join(map(str, my_cursor.fetchone()))

                
                self.draw_boundary(img, (startX, startY), (endX, endY), color, student_id, roll_no, student_name, department)
                self.mark_attendance(student_id, roll_no, student_name, department)
                
            else:
                color = (0, 0, 255)
                self.draw_boundary(img, startX, startY, endX, endY, color, "Unknown", "Unknown", "Unknown", "Unknown")

        return img


    def face_recog(self):
        self.face_net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')
        self.clf = cv2.face_LBPHFaceRecognizer.create()
        self.clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        cv2.namedWindow("Welcome To Face Recognition", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img)
            cv2.imshow("Welcome To Face Recognition", img)
            if not ret:
                print("Error: Could not capture frame.")
                break

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
