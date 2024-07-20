from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk   #pip install pillow
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1950x1000+0+0")
        self.root.config(bg="white")
        #-----------------bg image--------------------------
        self.bg=ImageTk.PhotoImage(file="photo/backround.jpeg")
        bg=Label(self.root,image=self.bg).place(x=250,y=50,width=1500,height=700)
       
        #-----------------left image--------------------------
        self.left=ImageTk.PhotoImage(file="photo/side.jpeg")
        left=Label(self.root,image=self.left).place(x=82,y=100,relwidth=550,relheight=650)
        #--------------Register Fream------------------
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #-----------------------Row1------------------------------
        self.var_fname=StringVar()
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=80,y=130,width=250)
         
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        
        #---------------------------------------Row2-----------
        
        contact=Label(frame1,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="yellow")
        self.txt_contact.place(x=50,y=200,width=250)
         
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=40,y=200,width=250)
          
        #----------------------------------Row3------------------
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your first pet name","Your best friend name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=40,y=270,width=250)
        
        #---------------------------------------Row4-----------
        
        password=Label(frame1,text="password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="yellow")
        self.txt_password.place(x=50,y=340,width=250)
         
        cpassword=Label(frame1,text="cpassword",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=40,y=340,width=250)
        
        #--------------------------Terms--------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Teram & Conditions",variable=self.var_chk,onvalue="1",offvalue="0",bg="white",font=("times new roman",12)).place(x=50,y=380)  
        
        self.btn_img=ImageTk.PhotoImage(file="photo/Logo.png")# register
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login=Button(self.root,text="Sign in",font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=180) 
    
    def register_data(self):
        print(self.var_fname.get())        
        
root=Tk()
obj=register(root)
root.mainloop()
