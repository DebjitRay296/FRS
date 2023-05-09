from tkinter import * #tkinter: a powerful module to make gui
from tkinter import ttk
import tkinter #ttk: has stylish tool kits
from tkinter import messagebox 
from PIL import Image,ImageTk #pillow: to import images.The more generalized formats are JPEG/JPG and PNG. To open and display with those formats,we need help of ImageTk and Image classes from PIL(photo imaging Library) package
import os
from student import Student
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from help import Help
from attendance import Attendance

class FaceRecognitionSystem:
    def __init__(self,root): #root for windows
        self.root=root #initialise root
        self.root.geometry("1920x1080") #to set the geometry for windows
        self.root.title("Face Recognition System") #title for windows
        self.root.attributes('-fullscreen', False)
        self.root.state("zoomed")

        # first img
        img=Image.open(r"images\tech11.gif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) #to open and display photos in png/jpg formats

        fLabel=Label(self.root,image=self.photoimg) # to set the image on windows
        fLabel.place(x=0,y=0,width=500,height=130) # to specify coordinates in windows

        # second img
        img1=Image.open(r"images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1) #to open and display photos in png/jpg formats

        fLabel=Label(self.root,image=self.photoimg1) # to set the image on windows
        fLabel.place(x=500,y=0,width=500,height=130) # to specify coordinates in windows

        # third img
        img2=Image.open(r"images\img.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2) #to open and display photos in png/jpg formats

        fLabel=Label(self.root,image=self.photoimg2) # to set the image on windows
        fLabel.place(x=1000,y=0,width=550,height=130) # to specify coordinates in windows

        # bg img
        img3=Image.open(r"images\136925179.jpg")
        img3=img3.resize((1600,800),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) #to open and display photos in png/jpg formats

        bgImg=Label(self.root,image=self.photoimg3) # to set the image on windows
        bgImg.place(x=0,y=130,width=1600,height=700) # to specify coordinates in windows

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

        # student button
        img4=Image.open(r"images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b11=Button(bgImg,text="Student Details",command=self.student_details,cursor="hand2",font=("arial",15,"bold"),bg="black",fg="yellow")
        b11.place(x=200,y=300,width=220,height=40)

        # Detect face button
        img5=Image.open(r"images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b11=Button(bgImg,text="Face Detector",cursor="hand2",command=self.face_data,font=("arial",15,"bold"),bg="black",fg="yellow")
        b11.place(x=500,y=300,width=220,height=40)

        # Attendance button
        img6=Image.open(r"images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b11=Button(bgImg,text="Attendance",cursor="hand2",command=self.attendance_data,font=("arial",15,"bold"),bg="black",fg="yellow")
        b11.place(x=800,y=300,width=220,height=40)

        # Help button
        img7=Image.open(r"images\help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b11=Button(bgImg,text="Help",cursor="hand2",font=("arial",15,"bold"),bg="black",fg="yellow",command=self.help_data)
        b11.place(x=1100,y=300,width=220,height=40)

        # Train Face button
        img8=Image.open(r"images\train.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b11=Button(bgImg,text="Train Data",cursor="hand2",command=self.train_data,font=("arial",15,"bold"),bg="black",fg="yellow")
        b11.place(x=200,y=580,width=220,height=40)

        # Photos button
        img9=Image.open(r"images\photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b11=Button(bgImg,text="Photos",cursor="hand2",command=self.open_img,font=("arial",15,"bold"),bg="black",fg="yellow")
        b11.place(x=500,y=580,width=220,height=40)

        # Developer button
        img10=Image.open(r"images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b11=Button(bgImg,text="Developer",cursor="hand2",command=self.developer_data,font=("arial",15,"bold"),bg="black",fg="yellow")
        b11.place(x=800,y=580,width=220,height=40)

        # Exit button
        img11=Image.open(r"images\logout.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11) #to open and display photos in png/jpg formats

        b1=Button(bgImg,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b11=Button(bgImg,text="Log Out",cursor="hand2",command=self.iExit,font=("arial",15,"bold"),bg="black",fg="yellow")
        b11.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to LogOut",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return






    # Function Buttons

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

    def attendance_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance(self.new_window)


if __name__ == "__main__":  #calling main
    root=Tk()  #calling root from toolkit
    obj=FaceRecognitionSystem(root) #creating object of class and joining to root
    root.mainloop()