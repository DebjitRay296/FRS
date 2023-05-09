from tkinter import * 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1920x1080")
        self.root.title("Face Recognition System")
        self.root.attributes('-fullscreen', False)
        self.root.state("zoomed")

        titleLbl=Label(self.root,text="TRAIN DATA SET",font=("Helvetica",35,"bold"),bg="yellow",fg="red")
        titleLbl.place(x=0,y=15,width=1530,height=45)

        img_top=Image.open(r"images\facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        fLabel=Label(self.root,image=self.photoimg_top)
        fLabel.place(x=0,y=55,width=1530,height=325)

        # Button

        b11=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("arial",30,"bold"),bg="red",fg="white")
        b11.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"images\opencv_face_reco_more_data.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        fLabel=Label(self.root,image=self.photoimg_bottom)
        fLabel.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Grayscale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train Classifier

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed.")




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()