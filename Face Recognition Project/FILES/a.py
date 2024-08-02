import cv2
import numpy as np
import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Student Details")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1300, height=40)

        img_top = Image.open("D:\\Face Recognition Project\\images\\face_detector1.jpg")
        img_top = img_top.resize((550, 600), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=550, height=600)

        img_bottom = Image.open(r"D:\Face Recognition Project\images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((750, 600), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_1 = Label(self.root, image=self.photoimg_bottom)
        f_lbl_1.place(x=550, y=40, width=750, height=600)

        b1_1 = Button(f_lbl_1, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=280, y=530, width=185, height=35)

    def mark_attendance(self, i, r, n, d):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if i not in name_list and r not in name_list and n not in name_list and d not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{d},{dtString},{d1},present\n")

    def draw_boundary(self, img, scaleFactor, minNeighbors, color, text):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (h, w) = img.shape[:2]

        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        self.face_net.setInput(blob)
        detections = self.face_net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype(int)

                face = gray_image[startY:endY, startX:endX]
                id, predict = self.clf.predict(face)

                conn = mysql.connector.connect(host="localhost", user="root", password="ROOT", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute(f"Select StudentName from student where StudentID = {id}")
                n = "+".join(map(str, my_cursor.fetchone()))

                my_cursor.execute(f"Select RollNo from student where StudentID = {id}")
                r = "+".join(map(str, my_cursor.fetchone()))

                my_cursor.execute(f"Select Department from student where StudentID = {id}")
                d = "+".join(map(str, my_cursor.fetchone()))

                my_cursor.execute(f"Select StudentID from student where StudentID = {id}")
                i = "+".join(map(str, my_cursor.fetchone()))


                if confidence > 30:
                    cv2.rectangle(img, (startX, startY), (endX, endY), color, 2)
                    cv2.putText(img, f"ID: {i}", (startX, startY - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (startX, startY - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (startX, startY - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (startX, startY - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)
                    cv2.putText(img, "Unknown", (startX, startY - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        return img

    def recognize(self, img):
        img = self.draw_boundary(img, 1.1, 10, (255, 25, 255), "Face")
        return img

    def face_recog(self):
        self.face_net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')
        self.clf = cv2.face_LBPHFaceRecognizer.create()
        self.clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        # Create a named window for displaying the image
        cv2.namedWindow("Welcome To Face Recognition", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

        while True:
            ret, img = video_cap.read()
            print("Capturing Frame....")
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
