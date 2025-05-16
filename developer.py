from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        

        # backgorund image 
        bg1=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\bg2.jpg")
        bg1=bg1.resize((1950,2500),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=-150,y=-250,width=1900,height=2500)



        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\IMG-20240701-WA0065.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=1130,y=550,width=180,height=180)

        std_b1_1 = Button(bg_img,text="SULIMAN",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=1130,y=730,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\raa.png")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=930,y=550,width=180,height=180)

        det_b1_1 = Button(bg_img,text="RAMI ",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=930,y=730,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\w..jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=730,y=550,width=180,height=180)

        att_b1_1 = Button(bg_img,text="HISHAM",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=730,y=730,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\DOC-20240220-WA0020_00001-1.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=530,y=550,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="AERFAN ",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=530,y=730,width=180,height=45)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
    