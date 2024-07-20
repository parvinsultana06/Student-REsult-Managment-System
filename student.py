from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class studentClass:
    def __init__(self,root):
       self.root=root
       self.root.title("Student Result Managment System")
       self.root.geometry("1200x480+250+100")
       self.root.config(bg="white")
       self.root.focus_force()
       
       #===title===
       title=Label(self.root,text="Manage student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=10,relwidth=1,height=40)
       
       #===Variables===
       self.var_roll=StringVar()
       self.var_name=StringVar()
       self.var_email=StringVar()
       self.var_gender=StringVar()
       self.var_dob=StringVar()
       self.var_contact=StringVar()
       self.var_addmission=StringVar()
       self.var_course=StringVar()
       self.var_state=StringVar()
       self.var_city=StringVar()
       #self.var_address=StringVar()
       self.var_duration=StringVar()
       self.var_charges=StringVar()
       
       
       #=====widgets======
       #=====column1======
       lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",20,"bold"),bg="white").place(x=5,y=80)
       lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=5,y=120)
       lbl_Email=Label(self.root,text="Email",font=("goudy old style",20,"bold"),bg="white").place(x=5,y=160)
       lbl_gender=Label(self.root,text="Gender",font=("goudy old style",20,"bold"),bg="white").place(x=5,y=200)
       lbl_state=Label(self.root,text="state",font=("goudy old style",20,"bold"),bg="white").place(x=5,y=240)
       txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=180,y=242,width=200)
       
       lbl_city=Label(self.root,text="City",font=("goudy old style",20,"bold"),bg="white").place(x=400,y=240)
       txt_city=Entry(self.root,textvariable=self.var_state,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=540,y=242,width=200)
       
       lbl_address=Label(self.root,text="Address",font=("goudy old style",20,"bold"),bg="white").place(x=5,y=280)
       
       #====Entry Fildes=====
       self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",20,"bold"),bg="lightyellow")
       self.txt_roll.place(x=180,y=70,width=200)
       txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=180,y=110,width=200)
       txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=180,y=150,width=200)
       self.txt_Gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"))
       self.txt_Gender.place(x=180,y=200,width=200)
       self.txt_Gender.current(0)
       
       
       
       
       #=====column2======
       lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",20,"bold"),bg="white").place(x=400,y=80)
       lbl_contact=Label(self.root,text="Contact",font=("goudy old style",20,"bold"),bg="white").place(x=400,y=120)
       lbl_addmission=Label(self.root,text="Addmission",font=("goudy old style",20,"bold"),bg="white").place(x=400,y=160)
       lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=400,y=200)
       
       
       #=====Entry fields=================================================
       self.course_list=[]
       #function call to update the list
       self.fetch_course()
       self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=535,y=60,width=200)
       txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=535,y=110,width=200)
       txt_addmission=Entry(self.root,textvariable=self.var_addmission,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=535,y=150,width=200)
       self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list)
       self.txt_course.place(x=535,y=200,width=200)
       self.txt_course.set("Select")
       
       
       #=========Text address========================
       
       self.txt_address=Text(self.root,font=("goudy old style",20,"bold"),bg="lightyellow")
       self.txt_address.place(x=180,y=280,width=550,height=110)
       
       #====Buttons====
       self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
       self.btn_add.place(x=180,y=400,width=110,height=40)
       self.btn_add=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
       self.btn_add.place(x=300,y=400,width=110,height=40)
       self.btn_add=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
       self.btn_add.place(x=420,y=400,width=110,height=40)
       self.btn_add=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
       self.btn_add.place(x=540,y=400,width=110,height=40)
       
       #===Serach Panel=======
       self.var_search=StringVar()
       lbl_search_roll=Label(self.root,text=" Roll No",font=("goudy old style",20,"bold"),bg="white").place(x=850,y=80)
       txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=1000,y=80,width=180)
       btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1350,y=80,width=180,height=35)
       
       
       #====content=====
       self.c_Frame=Frame(self.root,bd=2,relief=RIDGE)
       self.c_Frame.place(x=855,y=140,width=600,height=350)
       
       scrolly=Scrollbar(self.c_Frame,orient=VERTICAL)    #add  scrollbar
       scrollx=Scrollbar(self.c_Frame,orient=HORIZONTAL)
       
       self.CourseTable=ttk.Treeview(self.c_Frame,columns=("roll","name","email","gender","dob","contact","addmission","course","state","city","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)   # set columns
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.CourseTable.xview)
       scrolly.config(command=self.CourseTable.yview)
       
       self.CourseTable.heading("roll",text="Roll No")
       self.CourseTable.heading("name",text="Name")
       self.CourseTable.heading("email",text="Email")
       self.CourseTable.heading("gender",text="Gender")
       self.CourseTable.heading("dob",text="D.O.B")
       self.CourseTable.heading("contact",text="Contact")
       self.CourseTable.heading("addmission",text="Addmission")
       self.CourseTable.heading("course",text="Course")
       self.CourseTable.heading("state",text="State")
       self.CourseTable.heading("city",text="City")
       self.CourseTable.heading("address",text="Address")
       self.CourseTable["show"]='headings'
       self.CourseTable.column("roll",width=120)
       self.CourseTable.column("name",width=120)
       self.CourseTable.column("email",width=100)
       self.CourseTable.column("gender",width=100)
       self.CourseTable.column("dob",width=100)
       self.CourseTable.column("contact",width=100)
       self.CourseTable.column("addmission",width=100)
       self.CourseTable.column("course",width=100)
       self.CourseTable.column("state",width=100)
       self.CourseTable.column("city",width=100)
       self.CourseTable.column("address",width=200)
       self.CourseTable.pack(fill=BOTH,expand=1)
       self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
       self.show()
      
#=====================================================================================================================
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_addmission.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.txt_address.delete("1.0",END)   
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
        
    def delete(self):
         con=sqlite3.connect(database="Result Project.db")
         cur=con.cursor()
         try:
            if self.var_roll.get()=="":
              messagebox.showerror("Error","Roll no. should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student delete successfully",parent=self.root)
                        self.clear()
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
        
        
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_addmission.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.txt_address.delete("1.0",END)   
        self.txt_address.insert(END,row[10])
        
        
        
    def add(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
              messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,addmission,course,state,city,address)values(?,?,?,?,?,?,?,?,?,?,?)",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(), 
                    self.var_contact.get(),
                    self.var_addmission.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.txt_address.get("1.0",END)
                ))
                con.commit()
                messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
    def update(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error"," Select student from list",parent=self.root)
                else:
                    cur.execute("update student  set name=?,email=?,gender=?,dob=?,contact=?,addmission=?,course=?,state=?,city=?,address=? where roll=?",(
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(), 
                    self.var_contact.get(),
                    self.var_addmission.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.txt_address.get("1.0",END),
                    self.var_roll.get() 
                ))
                con.commit()
                messagebox.showinfo("Success","student Update  Successfully",parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
           
    def show(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    
    def fetch_course(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                     self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
    def search(self):
        con=sqlite3.connect(database="Result Project.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
               self.CourseTable.delete(*self.CourseTable.get_children())
               self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")        
           
       
       
if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()