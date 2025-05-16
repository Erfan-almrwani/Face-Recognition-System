from sys import path
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")
        # This part is image labels setting start 
        # first header image  
        # backgorund image 
        bg1=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\t_bg1.jpg")
        bg1=bg1.resize((1920,1000),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=-150,y=-100,width=1900,height=1080)
        #title section
        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\OIG2.jpg")
        std_img_btn=std_img_btn.resize((253,235),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)
        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=811,y=390)
        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="green")
        std_b1_1.place(x=850,y=635,width=180,height=45)

    # # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==10
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    app=Train()(root)
    root.mainloop()