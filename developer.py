from ctypes import alignment
from tkinter import * 
from tkinter import ttk
from turtle import update 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1920x1080")
        self.root.title("Face Recognition System")
        self.root.attributes('-fullscreen', False)
        self.root.state("zoomed")

        titleLbl=Label(self.root,text="DEVELOPED BY",font=("times new roman",35,"bold"),bg="yellow",fg="black")
        titleLbl.place(x=0,y=15,width=1530,height=45)

        img_top=Image.open(r"images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        fLabel=Label(self.root,image=self.photoimg_top)
        fLabel.place(x=0,y=55,width=1530,height=720)

        #Frame
        main_frame=Frame(fLabel,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"images\Debjit Ray.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        fLabel=Label(main_frame,image=self.photoimg_top1)
        fLabel.place(x=300,y=0,width=200,height=200)

        #Developer Info
        dev_label=Label(main_frame,text=" DEBJIT RAY",font=("times new roman",20,"bold"),fg="red",bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text=" DEBO",font=("times new roman",20,"bold"),fg="red",bg="white")
        dev_label.place(x=0,y=40)

        img2=Image.open(r"images\Debo.jpeg") 
        img2=img2.resize((200,200), Image.ANTIALIAS) 
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2) 
        f_lbl.place(x=8,y=210,width=500,height=390)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()