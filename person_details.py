import pandas as pd
import mysql.connector
from tkinter import *
import PySimpleGUI as sg
conn = mysql.connector.connect(user='root', password='kumar', host='127.0.0.1', database='liveproject',auth_plugin='mysql_native_password')
class person:
    def __init__(self,name,age,covid_status,family,vacc_status,address):
        self.name = name
        self.age = age
        self.covid_status = covid_status
        self.family = family
        self.vacc_status = vacc_status
        self.address = address
    def show(self):
        sg.Print("name = ",self.name,"\nage = ",self.age,"\ncovid status = ",self.covid_status,"\nfmembers = ","\nvacc_status = ",self.family)
        sg.Print("doorno = ",self.address.doorno,"\nstreetname = ",self.address.streetname,"\narea = ",self.address.area,"\ncity =",self.address.city)
    def data(self):
        
        info = [str(self.name),self.age,str(self.covid_status),self.family,self.vacc_status,
                str(self.address.doorno),str(self.address.streetname),str(self.address.area),str(self.address.city)]
        query = """insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor = conn.cursor()
        cursor.execute(query,info) 
        conn.commit()
        

class address:
    def __init__(self,doorno,streetname,area,city):
        self.doorno = doorno
        self.streetname = streetname
        self.area = area
        self.city = city



r = Tk()
r.title("covid details")
l = Label(r,text ="Personal Details",fg = "red",font = ("algerian",25))
l.grid(row = 0,column=2)

l1=Label(r,text="NAME :",font=('arial',20))
l1.grid(column=0,row=1,padx=20,pady=10,sticky=W)
e=Entry(r,width=50,font=('arial',20),bg="white",fg="black")
e.grid(column=2,row=1,padx=40,pady=10)

l2=Label(r,text="age :",font=('arial',20))
l2.grid(column=0,row=2,padx=20,pady=10,sticky=W)
e1=Entry(r,width=50,font=('arial',20),bg="white",fg="black")
e1.grid(column=2,row=2,padx=40,pady=10)

l3=Label(r,text="covid_status(yes or no):",font=('arial',20))
l3.grid(column=0,row=3,padx=20,pady=10,sticky=W)
e2=Entry(r,width=50,font=('arial',20),bg="white",fg="red")
e2.grid(column=2,row=3,padx=40,pady=10)



l5=Label(r,text="vaccine status(1 or 2) :",font=('arial',20))
l5.grid(column=0,row=5,padx=20,pady=10,sticky=W)
e4=Entry(r,width=50,font=('arial',20),bg="white",fg="green")
e4.grid(column=2,row=5,padx=40,pady=10)

l6=Label(r,text="doorno :",font=('arial',20))
l6.grid(column=0,row=6,padx=20,pady=10,sticky=W)
e5=Entry(r,width=50,font=('arial',20),bg="white",fg="black")
e5.grid(column=2,row=6,padx=40,pady=10)

l7=Label(r,text="streetname :",font=('arial',20))
l7.grid(column=0,row=7,padx=20,pady=10,sticky=W)
e6=Entry(r,width=50,font=('arial',20),bg="white",fg="black")
e6.grid(column=2,row=7,padx=40,pady=10)

l8=Label(r,text="area :",font=('arial',20))
l8.grid(column=0,row=8,padx=20,pady=10,sticky=W)
e7=Entry(r,width=50,font=('arial',20),bg="white",fg="black")
e7.grid(column=2,row=8,padx=40,pady=10)

l9=Label(r,text="city :",font=('arial',20))
l9.grid(column=0,row=9,padx=20,pady=10,sticky=W)
e8=Entry(r,width=50,font=('arial',20),bg="white",fg="black")
e8.grid(column=2,row=9,padx=40,pady=10)

l4=Label(r,text="family members :",font=('arial',20))
l4.grid(column=0,row=4,padx=20,pady=10,sticky=W)
e3=Entry(r,width=50,font=('arial',20),bg="white",fg="black")
e3.grid(column=2,row=4,padx=40,pady=10)

def submit():
    add1 = address(e5.get(),e6.get(),e7.get(),e8.get())
    p = person(e.get(),e1.get(),e2.get(),e3.get(),e4.get(),add1)
    p.show()
    p.data()
b = Button(r,text = "submit",command = submit,padx=20,pady=10,font = ("arial",15))
b.grid(column = 2,row=10)

def analytics():
    df = pd.read_sql_query("select  * from person",conn)
    df = pd.DataFrame(df)

    def effectedbyarea():
        
    #how many in city got effected due to covid 
        sg.Print("no of peope affected in ",e12.get()," = ",df[(df["covid_status"]=="yes" ) & (df["city"]==e12.get() )]["pname"].count())
    def covid_after_vaccination():
        sg.Print("covid after vaccination  =",df[(df["vaccination_status"]==2) & (df["covid_status"]=="yes" )]["pname"].count())
    def covid_after_50():
        sg.Print("covid after 50 =",df[(df["covid_status"]=="yes") & (df["age"]>50)]["city"].count())
    def citycount():
        sg.Print("covid in cities =",df["city"].value_counts().sort_values(ascending=True))
    def get_probability():
        sg.Print("these people have probability =",df[ (df["vaccination_status"] < 2) & (df["covid_status"]=="yes" ) ]["pname"].count())
    def get_data():
        sg.Print(df)
    r1 = Tk()
    r1.title("analytics menu")
    areaef = Label(r1,text="enter city to check no of peopel effected")
    areaef.pack()
    e12 = Entry(r1,width=50,font=('arial',20),bg="white",fg="black")
    e12.pack()
    
    b = Button(r1,text = "persons effected by area",command =effectedbyarea ,padx = 20,pady=10)
    b.pack()
    b1 = Button(r1,text = "covid after vaccination",command =covid_after_vaccination ,padx = 20,pady=10)
    b1.pack()
    b2 = Button(r1,text = "covid after 50",command = covid_after_50,padx = 20,pady=10)
    b2.pack()
    b3 = Button(r1,text = "city count",command =citycount,padx = 20,pady=10)
    b3.pack()
    b4 = Button(r1,text = "get probability",command =get_probability ,padx = 20,pady=10)
    b4.pack()
    b5 = Button(r1,text = "data",command =get_data ,padx = 20,pady=10)
    b5.pack()
    r1.mainloop()

b1 = Button(r,text = "Analytics",command =analytics,padx=20,pady=10,font = ("arial",15))
b1.grid(column=0,row=10)
r.mainloop()