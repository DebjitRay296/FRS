from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pyttsx3
import mysql.connector
import os
from time import strftime
from datetime import datetime
from main import FaceRecognitionSystem
from student import Student
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from help import Help
from attendance import Attendance
from register import Register



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window: 
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080")
        self.root.state("zoomed")

        #text to speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)

        self.var_email=StringVar()
        self.var_pass=StringVar()

        # first img
        img=Image.open(r"images\tech11.gif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) 
        fLabel=Label(self.root,image=self.photoimg) 
        fLabel.place(x=0,y=0,width=500,height=130) 

        # second img
        img11=Image.open(r"images\facialrecognition.png")
        img11=img11.resize((500,130),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11) 

        fLabel=Label(self.root,image=self.photoimg11) 
        fLabel.place(x=500,y=0,width=500,height=130) 

        # third img
        img22=Image.open(r"images\img.jpg")
        img22=img22.resize((550,130),Image.ANTIALIAS)
        self.photoimg22=ImageTk.PhotoImage(img22) 

        fLabel=Label(self.root,image=self.photoimg22) 
        fLabel.place(x=1000,y=0,width=550,height=130) 

        # bg img
        img33=Image.open(r"images\136925179.jpg")
        img33=img33.resize((1600,800),Image.ANTIALIAS)
        self.photoimg33=ImageTk.PhotoImage(img33) 

        bgImg=Label(self.root,image=self.photoimg33) 
        bgImg.place(x=0,y=90,width=1600,height=700) 

        titleLbl=Label(bgImg,text="FACE RECOGINITION ATTENDANCE SYSTEM",font=("Helvetica",35,"bold"),bg="white",fg="red")
        titleLbl.place(x=0,y=15,width=1530,height=45)

        #Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(titleLbl, font = ('times new roman', 14, 'bold'), background = 'white', foreground = 'black') 
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        downtitle=Label(self.root,text="Note: Enter Valid Username/Password",font=("Helvetica",15,"bold"),bg="white",fg="red")
        downtitle.place(x=0,y=760,width=1600,height=35)

        
        frame=Frame(self.root, bg="black")
        frame.place(x=610,y=190,width=340,height=450)

        img1=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\s2.png")
        img1=img1.resize((100, 120), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=190, width=100, height=100)

        get_str=Label(frame, text="Get Started", font=("times new roman",20,"bold"), fg="light green",bg="black")
        get_str.place(x=100,y=105)

        # label
        username=Label(frame,text="Username/Email", font=("times new roman", 15, "bold"), fg="white",bg="black")
        username.place(x=70,y=145)

        #self.txtuser=StringVar()
        #self.txtpass=StringVar()

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold")) 
        self.txtuser.place(x=40,y=180,width=270)

        password=lb1=Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black") 
        password.place(x=70,y=215)
        
        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #Icon Image
        img2=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\LoginIconAppl.png")
        img2=img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=340, width=25, height=25)

        img3=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\lock-512.png")
        img3=img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=410, width=25, height=25)

        #Login button
        loginbtn=Button(frame,cursor="hand2",command=self.login,text="Login",font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="yellow",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
        registerbtn.place(x=15,y=350,width=160)

        #ForgotPasswd Btn
        passwdbtn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="yellow",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
        passwdbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window) 

    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            self.engine.say('All Fields are Required')
            self.engine.runAndWait()
            messagebox.showerror("Error","All Fields Required")
        #elif self.txtuser.get()=="Admin" and self.txtpass.get()=="Admin":
            #messagebox.showinfo("Success","Welcome to the Portal")
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                            ))
                row=my_cursor.fetchone()
                if row==None:
                    self.engine.say('Invalid Credentials')
                    self.engine.runAndWait()
                    messagebox.showerror("Error","Invalid Username/Password")
                else:
                    self.engine.say('Welcome to the portal')
                    self.engine.runAndWait()
                    #messagebox.showinfo("Welcome",f"Welcome {self.txtuser.get()}")
                    self.new_window=Toplevel(self.root)
                    self.app=FaceRecognitionSystem(self.new_window)
            except Exception as es:
                messagebox.showerror("Error","Invalid Credentials")
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.var_email.set("")
        self.var_pass.set("")       

          
          
    #reset pass
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Enter Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password has been Changed Login with New Password",parent=self.root2)
                self.root2.destroy()


    #forgot password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            self.engine.say('Please Enter Email ID to reset password')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Email ID to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter valid Email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question", font=("times ren roman", 15, "bold"),bg="white") 
                security_Q.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"), state="readonly") 
                self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your School name", "Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

        
        
        
        
                security_A=Label (self.root2, text="Security Answer", font=("times new roman",15, "bold"),bg="white",fg="black") 
                security_A.place(x=50,y=150)
        
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15)) 
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label (self.root2, text="New Password", font=("times new roman",15, "bold"),bg="white",fg="black") 
                new_password.place(x=50,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15)) 
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15),fg="white",bg="green")
                btn.place(x=100,y=290,width=100)

            

# class Register:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Register")
#         self.root.geometry("1920x1080")
#         self.root.state("zoomed")
    
    #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar() 
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar() 
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
    
#     #bgimg
#         img=Image.open(r"images\bg.jpg")
#         img=img.resize((1600,800),Image.ANTIALIAS)
#         self.bgimg=ImageTk.PhotoImage(img)

#         bg_lbl=Label(self.root,image=self.bgimg)
#         bg_lbl.place(x=0,y=0)

#     #left img
#         self.bg1=ImageTk.PhotoImage(file=r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\a.jpeg") 
#         left_lbl=Label(self.root,image=self.bg1)
#         left_lbl.place(x=130,y=150,width=470,height=550)

#     #main frame  
#         frame=Frame(self.root,bg="white")
#         frame.place(x=600,y=150,width=800,height=550)

#     #label and entry

#         #row 1    
#         fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
#         fname.place(x=50,y=100)

#         self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
#         self.fname_entry.place(x=50,y=130,width=250)

#         l_name=Label(frame,text="Last Name", font=("times new roman", 15, "bold"), bg="white",fg="black") 
#         l_name.place(x=370,y=100)

#         self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15))
#         self.txt_lname.place(x=370,y=130,width=250)

#         #row 2

#         contact=Label(frame,text="Contact No", font=("times new roman", 15, "bold"), bg="white",fg="black") 
#         contact.place(x=50,y=170)
        
#         self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15)) 
#         self.txt_contact.place(x=50,y=200,width=250)

#         email=Label(frame,text="Email", font=("times new roman", 15, "bold"), bg="white",fg="black") 
#         email.place(x=370,y=170)

#         self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15)) 
#         self.txt_email.place(x=370,y=200,width=250)

#         #row 3
        
#         security_Q=Label(frame,text="Select Security Question", font=("times new roman", 15, "bold"),bg="white") 
#         security_Q.place(x=50,y=240)
        
#         self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"), state="readonly") 
#         self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your School name", "Your Pet Name")
#         self.combo_security_Q.place(x=50,y=270,width=250)
#         self.combo_security_Q.current(0)

        
        
        
        
#         security_A=Label (frame, text="Security Answer", font=("times new roman",15, "bold"),bg="white",fg="black") 
#         security_A.place(x=370,y=240)
        
#         self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15)) 
#         self.txt_security.place(x=370,y=270,width=250)

#         #row4

#         pswd=Label(frame, text="Password", font=("times new roman", 15, "bold"),bg="white", fg="black") 
#         pswd.place(x=50,y=310)
        
#         self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15)) 
#         self.txt_pswd.place(x=50,y=340, width=250)

#         confirm_pswd=Label(frame, text="Confirm Password",font=("times new roman", 15, "bold"),bg="white",fg="black") 
#         confirm_pswd.place(x=378,y=318)
#         self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15)) 
#         self.txt_confirm_pswd.place(x=370,y=340, width=250)

#         #check button
#         self.var_check=IntVar()
#         checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms And Conditions",font=("times new roman",12, "bold"),onvalue=1,offvalue=0)
#         checkbtn.place(x=50,y=380)

#         #buttons
#         img=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\registernowbutton1.jpg")
#         img=img.resize((200,50),Image.ANTIALIAS)
#         self.photoimage=ImageTk.PhotoImage(img)
#         b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
#         b1.place(x=10,y=420,width=200)

        
#         img1=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\login.png")
#         img1=img1.resize((200,50),Image.ANTIALIAS)
#         self.photoimage1=ImageTk.PhotoImage(img1)
#         b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
#         b1.place(x=330,y=420,width=200)



# Function Declaration
    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_lname.get()=="":
            self.engine.say('All Fields are Required')
            self.engine.runAndWait()
            messagebox.showerror("Error!!","All Fields are Required")
        elif self.var_contact.get()=="" or len(self.var_contact.get())!=10:
            self.engine.say('Enter 10 digit contact number')
            self.engine.runAndWait()
            messagebox.showerror("Error","Enter proper contact no")
        elif self.var_pass.get()=="" or len(self.var_pass.get())!=8:
            self.engine.say('Invalid password format')
            self.engine.runAndWait()
            messagebox.showerror("Error","Invalid password format Minimum 8 characters required")
        elif self.var_pass.get()!=self.var_confpass.get():
            self.engine.say('Password does not Match')
            self.engine.runAndWait()
            messagebox.showerror("Error","Password does not Match")
        elif self.var_check.get()==0:
            self.engine.say('Please Agree to the Terms and Conditions')
            self.engine.runAndWait()
            messagebox.showerror("Error","Agree to the Terms and Conditions")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="manager", database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
           
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successfull") 

    def return_login(self):
        self.root.destroy()

# class FaceRecognitionSystem:
#     def __init__(self,root): #root for windows
#         self.root=root #initialise root
#         self.root.geometry("1920x1080") #to set the geometry for windows
#         self.root.title("Face Recognition System") #title for windows
#         self.root.attributes('-fullscreen', False)
#         self.root.state("zoomed")

#         # first img
#         img=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\tech11.gif")
#         img=img.resize((500,130),Image.ANTIALIAS)
#         self.photoimg=ImageTk.PhotoImage(img) #to open and display photos in png/jpg formats

#         fLabel=Label(self.root,image=self.photoimg) # to set the image on windows
#         fLabel.place(x=0,y=0,width=500,height=130) # to specify coordinates in windows

#         # second img
#         img1=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\facialrecognition.png")
#         img1=img1.resize((500,130),Image.ANTIALIAS)
#         self.photoimg1=ImageTk.PhotoImage(img1) #to open and display photos in png/jpg formats

#         fLabel=Label(self.root,image=self.photoimg1) # to set the image on windows
#         fLabel.place(x=500,y=0,width=500,height=130) # to specify coordinates in windows

#         # third img
#         img2=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\img.jpg")
#         img2=img2.resize((550,130),Image.ANTIALIAS)
#         self.photoimg2=ImageTk.PhotoImage(img2) #to open and display photos in png/jpg formats

#         fLabel=Label(self.root,image=self.photoimg2) # to set the image on windows
#         fLabel.place(x=1000,y=0,width=550,height=130) # to specify coordinates in windows

#         # bg img
#         img3=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\136925179.jpg")
#         img3=img3.resize((1600,700),Image.ANTIALIAS)
#         self.photoimg3=ImageTk.PhotoImage(img3) #to open and display photos in png/jpg formats

#         bgImg=Label(self.root,image=self.photoimg3) # to set the image on windows
#         bgImg.place(x=0,y=130,width=1600,height=700) # to specify coordinates in windows

#         titleLbl=Label(bgImg,text="FACE RECOGINITION ATTENDANCE SYSTEM",font=("Helvetica",35,"bold"),bg="white",fg="red")
#         titleLbl.place(x=0,y=15,width=1530,height=45)

#         #Time
#         def time():
#             string=strftime('%H:%M:%S %p')
#             lbl.config(text = string)
#             lbl.after(1000, time)
            
#         lbl = Label(titleLbl, font = ('times new roman', 14, 'bold'), background = 'white', foreground = 'black') 
#         lbl.place(x=0,y=0,width=110,height=50)
#         time()

#         # student button
#         img4=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\student.jpg")
#         img4=img4.resize((220,220),Image.ANTIALIAS)
#         self.photoimg4=ImageTk.PhotoImage(img4) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg4,command=self.student_details,cursor="hand2")
#         b1.place(x=200,y=100,width=220,height=220)

#         b11=Button(bgImg,text="Student Details",command=self.student_details,cursor="hand2",font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=200,y=300,width=220,height=40)

#         # Detect face button
#         img5=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\face_detector1.jpg")
#         img5=img5.resize((220,220),Image.ANTIALIAS)
#         self.photoimg5=ImageTk.PhotoImage(img5) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg5,cursor="hand2",command=self.face_data)
#         b1.place(x=500,y=100,width=220,height=220)

#         b11=Button(bgImg,text="Face Detector",cursor="hand2",command=self.face_data,font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=500,y=300,width=220,height=40)

#         # Attendance button
#         img6=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\attendance.jpg")
#         img6=img6.resize((220,220),Image.ANTIALIAS)
#         self.photoimg6=ImageTk.PhotoImage(img6) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
#         b1.place(x=800,y=100,width=220,height=220)

#         b11=Button(bgImg,text="Attendance",cursor="hand2",command=self.attendance_data,font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=800,y=300,width=220,height=40)

#         # Help button
#         img7=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\help.jpg")
#         img7=img7.resize((220,220),Image.ANTIALIAS)
#         self.photoimg7=ImageTk.PhotoImage(img7) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg7,cursor="hand2",command=self.help_data)
#         b1.place(x=1100,y=100,width=220,height=220)

#         b11=Button(bgImg,text="Help",cursor="hand2",command=self.help_data,font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=1100,y=300,width=220,height=40)

#         # Train Face button
#         img8=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\train.png")
#         img8=img8.resize((220,220),Image.ANTIALIAS)
#         self.photoimg8=ImageTk.PhotoImage(img8) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg8,cursor="hand2",command=self.train_data)
#         b1.place(x=200,y=380,width=220,height=220)

#         b11=Button(bgImg,text="Train Data",cursor="hand2",command=self.train_data,font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=200,y=580,width=220,height=40)

#         # Photos button
#         img9=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\photos.jpg")
#         img9=img9.resize((220,220),Image.ANTIALIAS)
#         self.photoimg9=ImageTk.PhotoImage(img9) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg9,cursor="hand2",command=self.open_img)
#         b1.place(x=500,y=380,width=220,height=220)

#         b11=Button(bgImg,text="Photos",cursor="hand2",command=self.open_img,font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=500,y=580,width=220,height=40)

#         # Developer button
#         img10=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\developer.jpg")
#         img10=img10.resize((220,220),Image.ANTIALIAS)
#         self.photoimg10=ImageTk.PhotoImage(img10) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg10,cursor="hand2",command=self.developer_data)
#         b1.place(x=800,y=380,width=220,height=220)

#         b11=Button(bgImg,text="Developer",cursor="hand2",command=self.developer_data,font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=800,y=580,width=220,height=40)

#         # Exit button
#         img11=Image.open(r"images\logout.jpg")
#         img11=img11.resize((220,220),Image.ANTIALIAS)
#         self.photoimg11=ImageTk.PhotoImage(img11) #to open and display photos in png/jpg formats

#         b1=Button(bgImg,image=self.photoimg11,cursor="hand2",command=self.iExit)
#         b1.place(x=1100,y=380,width=220,height=220)

#         b11=Button(bgImg,text="Log Out",cursor="hand2",command=self.iExit,font=("arial",15,"bold"),bg="black",fg="yellow")
#         b11.place(x=1100,y=580,width=220,height=40)

    def student_details(self):
        self.new_window=Toplevel(self.root) 
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Face_Recognition(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Help(self.new_window)

    def open_img(self):
        os.startfile("data")

    def attendance_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to Log Out",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return         


if __name__ == "__main__":
    main()