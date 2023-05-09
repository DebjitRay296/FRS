from ctypes import alignment
from tkinter import * 
from tkinter import ttk
from turtle import update 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1920x1080")
        self.root.title("Face Recognition System")
        self.root.attributes('-fullscreen', False)
        self.root.state("zoomed")



        # Variable Declaration
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_batch=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
       
       
        # First Img
        img=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\Student1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) #to open and display photos in png/jpg formats

        fLabel=Label(self.root,image=self.photoimg) # to set the image on windows
        fLabel.place(x=0,y=0,width=500,height=130) # to specify coordinates in windows

        # Second Img
        img1=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\student2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1) #to open and display photos in png/jpg formats

        fLabel=Label(self.root,image=self.photoimg1) # to set the image on windows
        fLabel.place(x=500,y=0,width=500,height=130) # to specify coordinates in windows

        # Third Img
        img2=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\student3.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2) #to open and display photos in png/jpg formats

        fLabel=Label(self.root,image=self.photoimg2) # to set the image on windows
        fLabel.place(x=1000,y=0,width=550,height=130) # to specify coordinates in windows

        # Bg Img
        img3=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\bgimg.jpg")
        img3=img3.resize((1600,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) #to open and display photos in png/jpg formats

        bgImg=Label(self.root,image=self.photoimg3) # to set the image on windows
        bgImg.place(x=0,y=130,width=1600,height=700) # to specify coordinates in windows

        titleLbl=Label(bgImg,text="STUDENT MANAGEMENT SYSTEM",font=("Helvetica",35,"bold"),bg="yellow",fg="black")
        titleLbl.place(x=0,y=15,width=1530,height=45)

        main_frame=Frame(bgImg,bd=2)
        main_frame.place(x=0,y=62,width=1900,height=900)

        # Left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
        Left_frame.place(x=10,y=10,width=750,height=590)

        img_Left=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\s.jpg")
        img_Left=img_Left.resize((730,130),Image.ANTIALIAS)
        self.photoimg_Left=ImageTk.PhotoImage(img_Left)

        fLabel=Label(Left_frame,image=self.photoimg_Left)
        fLabel.place(x=5,y=0,width=730,height=130)
        
        # Current Course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Details",font=("Arial",12,"bold"))
        current_course_frame.place(x=5,y=140,width=750,height=150)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13, "bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Technology","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox (current_course_frame,textvariable=self.var_course,font=("times new roman", 13, "bold"),state="readonly")
        course_combo["values"]=("Select Course", "B.Tech", "M.Tech","BBA","MBA")
        course_combo.current (0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox (current_course_frame,textvariable=self.var_year,font=("times new roman", 13, "bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year", "1st", "2nd","3rd","4th")
        year_combo.current (0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox (current_course_frame,textvariable=self.var_semester,font=("times new roman", 13, "bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester", "1st", "2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current (0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student Information
        student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Information",font=("Arial",12,"bold"))
        student_frame.place(x=5,y=250,width=750,height=300)

        # Name
        studentName_label=Label(student_frame,text="Name:",font=("times new roman",13,"bold"))
        studentName_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
  
        studentName_entry=ttk.Entry(student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll No
        rollno_label=Label(student_frame,text="Roll No:",font=("times new roman",13,"bold"))
        rollno_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        rollno_entry=ttk.Entry(student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Batch
        Batch_label=Label(student_frame,text="Batch:",font=("times new roman",13,"bold"))
        Batch_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        batch_combo=ttk.Combobox (student_frame,textvariable=self.var_batch,font=("times new roman", 13, "bold"),state="readonly",width=18)
        batch_combo["values"]=("A1","A2","B1","B2")
        batch_combo.current (0)
        batch_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        # Gender
        gender_label=Label(student_frame,text="Gender:",font=("times new roman",13,"bold"))
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox (student_frame,textvariable=self.var_gender,font=("times new roman", 13, "bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current (0)
        gender_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)


        # Date of Birth
        dob_label=Label(student_frame,text="DOB:",font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,sticky=W)

        # Email ID
        email_label=Label(student_frame,text="Email ID:",font=("times new roman",13,"bold"))
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=3,padx=10,sticky=W)

        # Phone No
        phone_label=Label(student_frame,text="Phone No:",font=("times new roman",13,"bold"))
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,sticky=W)

        # Address
        address_label=Label(student_frame,text="Address:",font=("times new roman",13,"bold"))
        address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=3,column=3,padx=10,sticky=W)

        # Radio Button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Sample Photo",value="Yes")
        radiobutton1.grid(row=5,column=0)

        radiobutton2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Sample Photo",value="No")
        radiobutton2.grid(row=5,column=1)

        # Button Frame
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=725,height=35)

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        # Button Frame 1
        btn_frame1=Frame(student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=725,height=35)

        capturephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="CAPTURE",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        capturephoto_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn_frame1,text="DONT CAPTURE",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=1,column=1)



        # Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
        Right_frame.place(x=770,y=10,width=740,height=590)

        img_Right=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\s1.jpg")
        img_Right=img_Right.resize((730,130),Image.ANTIALIAS)
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)

        fLabel=Label(Right_frame,image=self.photoimg_Right)
        fLabel.place(x=5,y=0,width=730,height=130)

        # Search System
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("Arial",12,"bold"))
        Search_frame.place(x=5,y=135,width=740,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"))
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox (Search_frame,font=("times new roman", 13, "bold"),state="readonly",width=20)
        search_combo["values"]=("Select", "Roll No", "Phone No")
        search_combo.current (0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_btn=Button(Search_frame,text="SEARCH",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(Search_frame,text="SHOW ALL",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)
    
        # Table Frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=740,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dept.","Course","Year","Sem","Name","Roll No","Batch","Gender","DOB","Email","PhnNo","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept.",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Batch",text="Batch")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("PhnNo",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("Dept.",width=150)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=50)
        self.student_table.column("Sem",width=75)
        self.student_table.column("Name",width=200)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Batch",width=50)
        self.student_table.column("Gender",width=50)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=150)
        self.student_table.column("PhnNo",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # Function Declaration
    # Add Data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_batch.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get()
                                                                                                    
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    
    
    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_name.set(data[4])
        self.var_roll.set(data[5])
        self.var_batch.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])

    # Update Data
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update the Student Details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Batch=%s,Gender=%s,DOB=%s,Email_ID=%s,Phone_No=%s,Address=%s,Photo_Sample=%s where Roll_No=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_batch.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_roll.get()

                                                                                                                                                                                                                  ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Details updated successfully.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #Delete Data
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Roll No required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student's data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Roll_No=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)   
    # Reset Data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_batch.set("A1")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    # Take Photo Samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                for x in myresult:
                    id=self.var_roll.get()
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Batch=%s,Gender=%s,DOB=%s,Email_ID=%s,Phone_No=%s,Address=%s,Photo_Sample=%s where Roll_No=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_batch.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_roll.get()==id

                                                                                                                                                                                                               ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load haarcascade_frontalface_default.xml file from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    # Scaling Factor=1.3
                    # Minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data Set generation completed successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
