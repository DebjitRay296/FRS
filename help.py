from tkinter import * 
from tkinter import ttk
from turtle import update 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1920x1080")
        self.root.title("Face Recognition System")
        self.root.attributes('-fullscreen', False)
        self.root.state("zoomed")

        titleLbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="yellow",fg="black")
        titleLbl.place(x=0,y=12,width=1530,height=40)

        img_top=Image.open(r"images\ITSupport.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        fLabel=Label(self.root,image=self.photoimg_top)
        fLabel.place(x=0,y=55,width=1530,height=720)

        help_label=Label(fLabel,text=" Contact Us:",font=("times new roman",40,"bold"),fg="red",bg="white")
        help_label.place(x=550,y=260)

        help_label=Label(fLabel,text=" Email: abc@gmail.com",font=("times new roman",35,"bold"),fg="red",bg="white")
        help_label.place(x=550,y=360)

        help_label=Label(fLabel,text=" PH.No: 1234567890",font=("times new roman",35,"bold"),fg="red",bg="white")
        help_label.place(x=550,y=460)










if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()