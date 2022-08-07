from tkinter import *
from pymysql import *


class lenovo(Frame):
    def __init__(self,local):
        super().__init__(local)
        self.l0=Label(self,text="Please Enter Your Login Details ")
        self.l1=Label(self,text="Enter User Name ")
        self.l2=Label(self,text="Enter Password ")
        self.t1=Entry(self)
        self.t2=Entry(self,show="*")
        self.b1=Button(self,text="Login ",command=self.check)
        self.l0.grid(row=0,column=0)
        self.l1.grid(row=1,column=0)
        self.l2.grid(row=2,column=0)
        self.t1.grid(row=1,column=1)
        self.t2.grid(row=2,column=1)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        self.l0.grid(columnspan=2)
        self.b1.grid(columnspan=2)
        self.pack()
    def check(self):
        con=connect(db="office",user="root",password="root",host="localhost")
        cur=con.cursor()
        uid=self.t1.get()
        pwd=self.t2.get()
        cur.execute("select * from login where username ='%s' and password='%s'"%(uid,pwd))
        result=cur.fetchall()
        
        if(len(result)==1):
            from tkinter import messagebox as msg
            msg.showinfo("INFORMATION","thanks for login")
        else:
            from tkinter import messagebox as msg
            msg.showerror("ERROR","Wrong Password ")

root=Tk()
obj=lenovo(root)
root.title("Login Page")
root.geometry("400x300")
root.mainloop()


