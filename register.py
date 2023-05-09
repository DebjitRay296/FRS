from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pyttsx3
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1080")
        self.root.state("zoomed")

    #text to speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
    
    #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar() 
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar() 
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
    
    #bgimg
        img=Image.open(r"images\bg.jpg")
        img=img.resize((1600,800),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.bgimg)
        bg_lbl.place(x=0,y=0)

    #left img
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\regn.jpg") 
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=10,y=150,width=800,height=550)

    #main frame  
        frame=Frame(self.root,bg="white")
        frame.place(x=800,y=150,width=700,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",28,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

    #label and entry

        #row 1    
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name", font=("times new roman", 15, "bold"), bg="white",fg="black") 
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370,y=130,width=250)

        #row 2

        contact=Label(frame,text="Contact No", font=("times new roman", 15, "bold"), bg="white",fg="black") 
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15)) 
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email", font=("times new roman", 15, "bold"), bg="white",fg="black") 
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15)) 
        self.txt_email.place(x=370,y=200,width=250)

        #row 3
        
        security_Q=Label(frame,text="Select Security Question", font=("times ren roman", 15, "bold"),bg="white") 
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"), state="readonly") 
        self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your School name", "Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        
        
        
        
        security_A=Label (frame, text="Security Answer", font=("times new roman",15, "bold"),bg="white",fg="black") 
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15)) 
        self.txt_security.place(x=370,y=270,width=250)

        #row4

        pswd=Label(frame, text="Password", font=("times new roman", 15, "bold"),bg="white", fg="black") 
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15)) 
        self.txt_pswd.place(x=50,y=340, width=250)

        confirm_pswd=Label(frame, text="Confirm Password",font=("times new roman", 15, "bold"),bg="white",fg="black") 
        confirm_pswd.place(x=378,y=318)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15)) 
        self.txt_confirm_pswd.place(x=370,y=340, width=250)

        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms And Conditions",font=("times new roman",12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #buttons
        img=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\registernowbutton1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        
        img1=Image.open(r"C:\Users\u\OneDrive\Desktop\Face Recognition System\images\login.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)



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
        elif self.var_pass.get()=="":
            self.engine.say('Password Required')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please enter password")
        elif len(self.var_pass.get())!=8:
            self.engine.say('Password length too small')
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
                self.engine.say('User Already Exist')
                self.engine.runAndWait()
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
            self.engine.say('Registration Sucessful')
            self.engine.runAndWait()
            messagebox.showinfo("Success","Registration Successfull")
            




if __name__ == "__main__":
     root=Tk()
     app=Register(root)
     root.mainloop()