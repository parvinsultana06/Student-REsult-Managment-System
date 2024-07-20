from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3
import os
from tkinter import messagebox,ttk
class resultproject:
    def __init__(self,root):
       self.root=root
       self.root.title("Student Result Managment System")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="white")
       #===icons====
       #===title====
       title=Label(self.root,text="Student Result Managment System",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
       #===Menu====
       M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
       M_Frame.place(x=10,y=70,width=1340,height=80)
       
       
       btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
       btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
       btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
       btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
       btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
       btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)
            
       #===content_window===
       self.backround_img=Image.open("images/backround.png")  
       self.backround_img=self.backround_img.resize((920,350),Image.Resampling.LANCZOS)
       self.backround_img=ImageTk.PhotoImage(self.backround_img)
        
       self.lbl_bg=Label(self.root,image=self.backround_img).place(x=500,y=280,width=920,height=350)   
       
       #===update_details===
       self.lbl_course=Label(self.root,text="Total courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
       self.lbl_course.place(x=500,y=630,width=300,height=100) 
       
       self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
       self.lbl_student.place(x=810,y=630,width=300,height=100) 
       
       self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
       self.lbl_result.place(x=1120,y=630,width=300,height=100) 
       
       
       #=================Clock=======================
       self.lbl=Label(self.root,text="\nMy clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923")
       self.lbl.place(x=17,y=175,height=450,width=350)
       self.working()
        
        
       #===footer====
       footer=Label(self.root,text="SRMS-Student Result Managment System\nContact Us for any Technical Issue: 9064xxxx66",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
       self.update_details()
       
       #============================================================================================================
       
    def update_details(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")
            
            
            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def working(self): 
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min=(m/60)*360
        sec=(s/60)*360
        self.clock_image(hr,min,sec)
        self.img=ImageTk.PhotoImage(file="Images/watch_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
    def clock_image(self,hr,min,sec):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        # ======For clock Image===============#
        bg=Image.open("Images/Analog watch.png")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))
        #formula to rotate the Anticlock
        #angle_in_radians = angle_in_degrees * math.pi /180
        #line_length = 100
        #center_x = 250
        #center_y = 250
        #end_x = center_x + line_length * math.cos(angle_in_radians)
        #end_y = center_y + line_length * math.sin(angle_in_radians) 
       
        #======================== Hour  Line Image====================
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #=== Min  Line Image====================
        draw.line((origin,200+80*sin(radians(min)),200-80*cos(radians(min))),fill="blue",width=3)
        #=== Secound  Line Image====================
        draw.line((origin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="green",width=4)
        clock.save("Images/watch_new.png")  
       
    def add_course(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=CourseClass(self.new_win) 
        
        
    def add_student(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=studentClass(self.new_win)     
        
    def add_result(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=resultClass(self.new_win)     
        
    def add_report(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=reportClass(self.new_win) 
        
    def logout(self):
        op=messagebox. askyesno("Confirm","Do you really want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
            
    def exit_(self):
        op=messagebox. askyesno("Confirm","Do you really want to Exit?", parent=self.root)
        if op==True:
            self.root.destroy()
            
               
        
        
if __name__=="__main__":
    root=Tk()
    obj=resultproject(root)
    root.mainloop()