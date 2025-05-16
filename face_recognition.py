# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Face_Recognition:

    def __init__(self,root):
            self.root=root
            self.root.geometry("1366x768+0+0")
            self.root.title("Face Recognition Pannel")

            # This part is image labels setting start 
            # first hseader image  
            
            # backgorund image 
            bg1=Image.open(r"E:\\courses\\project paython\\Python-FYP-Face-Recognition-Attendence-System-master\\Images_GUI\\bg4.png")
            bg1=bg1.resize((1920,1000),Image.Resampling.LANCZOS)
            self.photobg1=ImageTk.PhotoImage(bg1)

            # set image as lable
            bg_img = Label(self.root,image=self.photobg1)
            bg_img.place(x=-150,y=-100,width=1900,height=1080)
            # Create buttons below the section 
            # ------------------------------------------------------------------------------------------------------------------- 
            # Training button 1
            std_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\OIG4.jpg")
            std_img_btn=std_img_btn.resize((300,300),Image.Resampling.LANCZOS)
            self.std_img1=ImageTk.PhotoImage(std_img_btn)

            std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
            std_b1.place(x=790,y=300)

        #=====================Attendance===================

    def mark_attendance(self,i,r,n):
            with open("E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\\attendance.csv","r+",newline="\n") as f:
                myDatalist=f.readlines()
                name_list=[]
                for line in myDatalist:
                    entry=line.split((","))
                    name_list.append(entry[0])

                if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


        #================face recognition==================
    def face_recog(self):
            def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]
                
                for (x,y,w,h) in featuers:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                    confidence=int((100*(1-predict/300)))

                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    cursor = conn.cursor()

                    cursor.execute("select Name from person where Person_ID="+str(id))
                    n=cursor.fetchone()
                    n=str(n)

                    cursor.execute("select NID from person where Person_ID="+str(id))
                    r=cursor.fetchone()
                    r = str(r)

                    cursor.execute("select Address from person where Person_ID="+str(id))
                    i=cursor.fetchone()
                    i = str(i)

                    if n == "None" or r == "None" or  i == "None":
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    elif confidence>77:
                        cv2.putText(img, f"Name:{i}",(x,y-100),cv2.FONT_ITALIC,0.8,(255,255,255),3)
                        cv2.putText(img, f"NID:{r}",(x,y-65),cv2.FONT_ITALIC,0.8,(255,255,255),3)
                        cv2.putText(img, f"Address:{n}",(x,y-30),cv2.FONT_ITALIC,0.8,(255,255,255),3)
                        
                        self.mark_attendance(i,r,n)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,h]
                
                return coord    


            #==========
            def recognize(img,clf,faceCascade):
                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
            
            faceCascade=cv2.CascadeClassifier("E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("clf.xml")

            videoCap=cv2.VideoCapture(0)
            adr= "http://192.168.43.1:4747/video"
            #adsr= "http://192.168.137.196:4747/video"
            videoCap.open(adr)
            
            #videoCap.open(adsr) 
            while True:
                ret,img=videoCap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Face Detector",img)

                if cv2.waitKey(1) == 13:
                    break
            videoCap.release()
            cv2.destroyAllWindows()
if __name__ == "__main__":
    root=Tk()
    app=Face_Recognition(root)
    root.mainloop()
