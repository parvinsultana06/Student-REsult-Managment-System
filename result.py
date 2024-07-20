from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
       self.root=root
       self.root.title("Student Result Managment System")
       self.root.geometry("1200x480+250+100")
       self.root.config(bg="white")
       self.root.focus_force()
       
       #===title===
       title=Label(self.root,text="Add Student Result ",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=10,relwidth=1,height=55)
       
       #=======widgets===============
       
       #===Variables===
       self.var_roll=StringVar()
       self.var_name=StringVar()
       self.var_course=StringVar()
       self.var_marks=StringVar()
       self.var_full_marks=StringVar()
       self.roll_list=[]
       self.fetch_roll()
       
       lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=80)
       lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=120)
       lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
       lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=200)
       lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=240)
       
       
       self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
       self.txt_student.place(x=325,y=90,width=180)
       self.txt_student.set("Select")
       btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=520,y=90,width=100,height=30)
       
       txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=325,y=130,width=300)
       txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=325,y=170,width=300)
       txt_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=325,y=210,width=300)
       txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=325,y=250,width=300)
       
       
       #====Buttons====
       btn_add=Button(self.root,text='Submit',font=("times new roman",15),bg="#f44336",cursor="hand2",command=self.add).place(x=350,y=320,width=120,height=40)
       btn_clear=Button(self.root,text='Clear',font=("times new roman",15),bg="#4caf50",cursor="hand2",command=self.clear).place(x=490,y=320,width=120,height=40)
       
       
       
       #=====image======
       self.backround_img=Image.open("images/Result.png")  
       self.backround_img=self.backround_img.resize((500,300),Image.ANTIALIAS)
       self.backround_img=ImageTk.PhotoImage(self.backround_img)
       
       self.lbl_bg=Label(self.root,image=self.backround_img).place(x=700,y=100) 

#====================================================================================================================       
       
    def fetch_roll(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            cur.execute("select  roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                     self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
                    
    def search(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            cur.execute(f"select  name, course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
               self.var_name.set(row[0])
               self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")       
            
            
            
    def add(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
              messagebox.showerror("Error","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per)values(?,?,?,?,?,?)",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get(), 
                    str(per)
                ))
                con.commit()
                messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
             
             
             
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

            
        
       
if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()