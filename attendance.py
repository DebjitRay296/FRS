from ctypes import alignment
from multiprocessing import Barrier
from tkinter import * 
from tkinter import ttk
from turtle import update 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import pyttsx3

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1920x1080")
        self.root.title("Face Recognition System")
        self.root.attributes('-fullscreen', False)
        self.root.state("zoomed")

        #text to speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)

        # Variables
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dept=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_attendance=StringVar()

        # First Img
        img=Image.open(r"images\student2.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) 

        fLabel=Label(self.root,image=self.photoimg)
        fLabel.place(x=0,y=0,width=800,height=200)

        # Second Img
        img1=Image.open(r"images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        fLabel=Label(self.root,image=self.photoimg1)
        fLabel.place(x=800,y=0,width=800,height=200)

        # Bg Img
        img3=Image.open(r"images\bgimg.jpg")
        img3=img3.resize((1600,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bgImg=Label(self.root,image=self.photoimg3)
        bgImg.place(x=0,y=200,width=1600,height=700)

        titleLbl=Label(bgImg,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Helvetica",35,"bold"),bg="#ecc19c",fg="#1e847f")
        titleLbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bgImg,bd=2)
        main_frame.place(x=15,y=62,width=1500,height=900)

        # Left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("Arial",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=590)

        img_Left=Image.open(r"images\face-recognition.png")
        img_Left=img_Left.resize((700,130),Image.ANTIALIAS)
        self.photoimg_Left=ImageTk.PhotoImage(img_Left)

        fLabel=Label(Left_frame,image=self.photoimg_Left)
        fLabel.place(x=5,y=0,width=700,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=180,width=700,height=300)

        # Labels and Entry

        # Roll
        roll_label=Label(left_inside_frame,text="Roll:",bg="white",font=("times new roman",13,"bold"))
        roll_label.grid(row=0,column=1,padx=4,pady=8)
  
        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=0,column=2,padx=4,pady=8)

        # Name
        name_label=Label(left_inside_frame,text="Name:",bg="white",font=("times new roman",13,"bold"))
        name_label.grid(row=0,column=3,padx=4,pady=8)
  
        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=0,column=4,padx=4,pady=8)

        # Department
        dept_label=Label(left_inside_frame,text="Department:",bg="white",font=("times new roman",13,"bold"))
        dept_label.grid(row=1,column=1,padx=4,pady=8)
  
        dept_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dept,font=("times new roman",13,"bold"))
        dept_entry.grid(row=1,column=2,padx=4,pady=8)

        # Date
        date_label=Label(left_inside_frame,text="Date:",bg="white",font=("times new roman",13,"bold"))
        date_label.grid(row=1,column=3,padx=4,pady=8)
  
        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=1,column=4,padx=4,pady=8)

        # Time
        time_label=Label(left_inside_frame,text="Time:",bg="white",font=("times new roman",13,"bold"))
        time_label.grid(row=2,column=1,padx=4,pady=8)
  
        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=2,padx=4,pady=8)

        # Attendance
        atten_label=Label(left_inside_frame,text="Attendance:",bg="white",font=("times new roman",13,"bold"))
        atten_label.grid(row=2,column=3)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=2,column=4,pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=725,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="UPDATE",width=17,command=self.updateCsv,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        # Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("Arial",12,"bold"))
        Right_frame.place(x=740,y=10,width=740,height=590)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=725,height=480)

        # Scroll Bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","department","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("roll",width=150)
        self.AttendanceReportTable.column("name",width=200)
        self.AttendanceReportTable.column("department",width=200)
        self.AttendanceReportTable.column("date",width=150)
        self.AttendanceReportTable.column("time",width=150)
        self.AttendanceReportTable.column("attendance",width=150)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # Fetch Data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data has been exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    # Update CSV
    def updateCsv(self):
        f=open("attendance.csv","r")
        csv_read=csv.reader(f)
        empty=[]
        for row in csv_read:
            if row[0]==self.var_atten_roll.get():
                row[5]=self.var_atten_attendance.get()
            empty.append(row)
        f.close()

        f=open("attendance.csv","w+",newline='')
        csv_write=csv.writer(f)
        csv_write.writerows(empty)
        self.engine.say('Attendance details updated successfully')
        self.engine.runAndWait()
        messagebox.showinfo("Success","Attendance details updated successfully")
        f.close()

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_roll.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dept.set(rows[2])
        self.var_atten_date.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_attendance.set(rows[5])

    # Reset Function
    def reset_data(self):
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dept.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()