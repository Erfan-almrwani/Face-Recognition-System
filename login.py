from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector
# --------------------------

from train import Train
from person import Person
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_pwd=StringVar()
        
        img=Image.open(r"E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\loginBg1.jpg")
        img=img.resize((1920,1080),Image.Resampling.LANCZOS)
        self.bg=ImageTk.PhotoImage(img)

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=-280,y=-158 )

        
        
        frame1= Frame(self.root,bg="#0F1B32")
        frame1.place(x=333,y=170,width=699,height=365)

        
       
        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="#5FCFC7",bg="#0F1B32")
        get_str.place(x=330,y=50)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="#5FCFC7",bg="#0F1B32")
        username.place(x=225,y=100)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=225,y=130,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="#5FCFC7",bg="#0F1B32")
        pwd.place(x=225,y=170)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=225,y=200,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#5FCFC7",bg="#0F1B32",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=225,y=250,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#5FCFC7",bg="#0F1B32",activeforeground="white",activebackground="#002B53")
        loginbtn.place(x=225,y=300,width=270,height=35)


        # Creating Button Forget
        

    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where fname=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                
                    return
            conn.commit()
            conn.close()


# =====================main program Face deteion system====================


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
        self.app=Person(self.new_window)

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
        self.app=Login(self.new_window)

   
    


  




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()
        
        bg1=Image.open(r"E:\\courses\\project paython\\Python-FYP-Face-Recognition-Attendence-System-master\\Images_GUI\\bgReg.jpg")
        bg1=bg1.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=-230,y=-230, width=1920,height=1080)

        
        frame1= Frame(self.root,bg="#0F1B32",border="5")
        frame1.place(x=430,y=180,width=570,height=500)
        
        # img1=Image.open(r"C:\Users\Muhammad Waseem\Documents\Python_Test_Projects\Images_GUI\reg1.png")
        # img1=img1.resize((450,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)
        
        get_str = Label(frame1,text="Registration",font=("times new roman",30,"bold"),fg="#fff",bg="#0F1B32")
        get_str.place(x=210,y=10)

        #label1 
        fname =lb1= Label(frame1,text="First Name:",font=("times new roman",15,"bold"),fg="#fff",bg="#0F1B32")
        fname.place(x=165,y=70)

        #entry1 
        self.txtuser=ttk.Entry(frame1,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=168,y=100,width=270)


        #label2 
        lname =lb1= Label(frame1,text="Last Name:",font=("times new roman",15,"bold"),fg="#fff",bg="#0F1B32")
        lname.place(x=165,y=130)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=168,y=160,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame1,text="N.I.D:",font=("times new roman",15,"bold"),fg="#fff",bg="#0F1B32")
        cnum.place(x=165,y=190)

        #entry1 
        self.txtuser=ttk.Entry(frame1,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=168,y=220,width=270)


       

        # ========================= Section 3 --- 1 Columan=================

       

        #label1 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="#fff",bg="#0F1B32")
        pwd.place(x=165,y=250)

        #entry1 
        self.txtuser=ttk.Entry(frame1,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=168,y=280,width=270)


        #label2 
        cpwd =lb1= Label(frame1,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#fff",bg="#0F1B32")
        cpwd.place(x=165,y=310)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=168,y=340,width=270)

        # Checkbutton
      
        # Creating Button Register
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=165,y=390,width=270,height=35)

        # Creating Button Login
        loginbtn=Button(frame1,command=self.log,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=165,y=450,width=270,height=35)
    
    def log(self):
        self.new_window=Toplevel(self.root)
        self.app=Login(self.new_window)
        
    
    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        
        else:
            messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',)
                mycursor = conn.cursor()
                query=("select * from regteach where cnum=%s")
                value=(self.var_cnum.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another N.I.D")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_pwd.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()
