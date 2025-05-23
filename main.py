from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from person import Person
from login import Login
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")
        
        
# This part is image labels setting start 
        
        # backgorund image 
        bg1=Image.open(r"E:\\courses\\project paython\\Python-FYP-Face-Recognition-Attendence-System-master\\Images_GUI\\OIG3.jpg")
        bg1=bg1.resize((2500,2500),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        # set image as lable
    
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=-10,y=-10,width=2500,height=2500)


        
        
        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"E:\\courses\\project paython\\Python-FYP-Face-Recognition-Attendence-System-master\\Images_GUI\\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.person_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.person_pannels,text="Person Pannel",cursor="hand2",font=("tahoma",15,"bold"),bg="#062341",fg="#1ED5F3")
        std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"E:\\courses\\project paython\\Python-FYP-Face-Recognition-Attendence-System-master\\Images_GUI\\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="#062341",fg="#1ED5F3")
        det_b1_1.place(x=480,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="#062341",fg="#1ED5F3")
        att_b1_1.place(x=710,y=280,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.helpSupport,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=100,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="Help Support",cursor="hand2",font=("tahoma",15,"bold"),bg="#062341",fg="#1ED5F3")
        hlp_b1_1.place(x=940,y=280,width=180,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=250,y=330,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("tahoma",15,"bold"),bg="#062341",fg="#1ED5F3")
        tra_b1_1.place(x=250,y=510,width=180,height=45)

        # Photo   button 6
        

        # Developers   button 7
        dev_img_btn=Image.open(r"E:\courses\\project paython\\Python-FYP-Face-Recognition-Attendence-System-master\\Images_GUI\\dev.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=600,y=330,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("tahoma",15,"bold"),bg="#062341",fg="#1ED5F3")
        dev_b1_1.place(x=600,y=510,width=180,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.LOGIN,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=940,y=330,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.LOGIN(),text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="#062341",fg="#1ED5F3")
        exi_b1_1.place(x=940,y=510,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")
# ==================Functions Buttons=====================
    def person_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Person()(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)
    
    def LOGIN(self):
        self.new_window=Toplevel(self.root)
        self.app=Login()(self.new_window)

   
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
