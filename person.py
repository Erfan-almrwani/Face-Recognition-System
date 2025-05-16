from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np


class Person:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Person Pannel")

        #-----------Variables-------------------
        self.var_per_id=StringVar()
        self.var_per_name=StringVar()
        self.var_lastname=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()

    # This part is image labels setting start 
        # first header image  
      

         # backgorund image 
        bg1=Image.open(r"E:\\courses\\project paython\\Python-FYP-Face-Recognition-Attendence-System-master\\Images_GUI\\bg3.jpg")
        bg1=bg1.resize((2000,1968),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0)


        #title section
        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=90,y=170,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Person-Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        
        #Class Student Information
        class_Person_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Person-Information",font=("verdana",12,"bold"),fg="navyblue")
        class_Person_frame.place(x=10,y=25,width=635,height=230)

        #Student id
        personId_label = Label(class_Person_frame,text="Per-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        personId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        personId_entry = ttk.Entry(class_Person_frame,textvariable=self.var_per_id,width=15,font=("verdana",12,"bold"))
        personId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        #persont name
        person_name_label = Label(class_Person_frame,text="Per-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        person_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        person_name_entry = ttk.Entry(class_Person_frame,textvariable=self.var_per_name,width=15,font=("verdana",12,"bold"))
        person_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        #persono
        person_roll_label = Label(class_Person_frame,text="NID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        person_roll_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)
        person_roll_entry = ttk.Entry(class_Person_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        person_roll_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)
        #person
        person_gender_label = Label(class_Person_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        person_gender_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Person_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

       
        #Email
        person_email_label = Label(class_Person_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        person_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        person_email_entry = ttk.Entry(class_Person_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        person_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        #personNumber
        person_mob_label = Label(class_Person_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        person_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)
        person_mob_entry = ttk.Entry(class_Person_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        person_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)
        #persons
        person_address_label = Label(class_Person_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        person_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)
        person_address_entry = ttk.Entry(class_Person_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        person_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        person_tutor_label = Label(class_Person_frame,text="Last Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        person_tutor_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        person_tutor_entry = ttk.Entry(class_Person_frame,textvariable=self.var_lastname,width=15,font=("verdana",12,"bold"))
        person_tutor_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        #Teacher Name

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Person_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(class_Person_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)
        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Person Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.person_table = ttk.Treeview(table_frame,column=("ID","Name","Lastname","Mob-No","Address","NID","Email","Gender","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.person_table.xview)
        scroll_y.config(command=self.person_table.yview)

        self.person_table.heading("ID",text="Person-ID")
        self.person_table.heading("Name",text="Name")
        self.person_table.heading("Lastname",text="Last-Name")
        self.person_table.heading("Mob-No",text="Mob-No")
        self.person_table.heading("Address",text="Address")
        self.person_table.heading("NID",text="NID")
        self.person_table.heading("Email",text="Email")
        self.person_table.heading("Gender",text="Gender")
        self.person_table.heading("Photo",text="PhotoSample")
        self.person_table["show"]="headings"
        # Setpersonof Colums 
        self.person_table.column("ID",width=100)
        self.person_table.column("Name",width=100)
        self.person_table.column("Gender",width=100)
        self.person_table.column("Mob-No",width=100)
        self.person_table.column("Address",width=100)
        self.person_table.column("NID",width=100)
        self.person_table.column("Email",width=100)
        self.person_table.column("Lastname",width=100)
        self.person_table.column("Photo",width=100)
        self.person_table.pack(fill=BOTH,expand=1)
        self.person_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Decleration==============================
    def add_data(self):
        if self.var_per_id.get()=="" or self.var_per_name.get()=="" or self.var_lastname.get()=="" or self.var_mob.get()==""   or self.var_address.get()=="" or self.var_roll.get()=="" or  self.var_email.get()=="" or self.var_gender.get()==""  :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_per_id.get(),
                self.var_per_name.get(),
                self.var_lastname.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from person")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.person_table.delete(*self.person_table.get_children())
            for i in data:
                self.person_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.person_table.focus()
        content = self.person_table.item(cursor_focus)
        data = content["values"]

        self.var_per_id.set(data[0]),
        self.var_per_name.set(data[1]),
        self.var_lastname.set(data[2]),
        self.var_mob.set(data[3]),
        self.var_address.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_email.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_radio1.set(data[8])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_per_id.get()=="" or self.var_per_name.get()=="" or self.var_lastname.get()=="" or self.var_mob.get()==""   or self.var_address.get()=="" or self.var_roll.get()=="" or  self.var_email.get()=="" or self.var_gender.get()==""  :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Person Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor()
                    mycursor.execute("update person set Name=%s,Lastname=%s,Mobile_No=%s,Address=%s,NID=%s,Email=%s,Gender=%s,PhotoSample=%s where Person_ID=%s",( 
                    self.var_per_name.get(),
                    self.var_lastname.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_radio1.get(),
                    self.var_per_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_per_id.get()=="":
            messagebox.showerror("Error","Person Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor() 
                    sql="delete from person where Person_ID=%s"
                    val=(self.var_per_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_per_id.set(""),
        self.var_lastname.set(""),
        self.var_per_name.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_gender.set("Male"),
        self.var_radio1.set("")
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                my_cursor = conn.cursor()
                sql = "SELECT Person_ID,Name,Lastname,Mobile_No,Address,NID,Email,Gender,PhotoSample FROM person where Name=" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.person_table.delete(*self.person_table.get_children())
                    for i in rows:
                        self.person_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if  self.var_per_id.get()=="" or self.var_per_name.get()=="" or self.var_lastname.get()=="" or self.var_mob.get()==""   or self.var_address.get()=="" or self.var_roll.get()=="" or  self.var_email.get()=="" or self.var_gender.get()==""  :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("select * from person")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update person set Name=%s,Lastname=%s,Mobile_No=%s,Address=%s,NID=%s,Email=%s,Gender=%s,PhotoSample=%s where Person_ID=%s",( 
                    self.var_per_name.get(),
                    self.var_gender.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_lastname.get(),
                    self.var_radio1.get(),
                    self.var_per_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                # if(cap.isOpened()== alse):
                #     print('the camera is close')
                
                
                cap=cv2.VideoCapture(0)
                adr= "http://192.168.43.1:4747/video"
                #adsr= "http://192.168.137.111:4747/video"
                #adr= "http://10.0.24.5:4747/video"
                cap.open(adr)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(600,600))
                        #face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="E:\courses\project paython\Python-FYP-Face-Recognition-Attendence-System-master\data_img\person."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==12 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Person(root)
    root.mainloop()
    
