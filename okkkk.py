# module from python library

from tkinter import *   # tkinter for GUI
from decimal import Decimal  #for round figur of cgpa and tga
import sqlite3   #for database work
from tkinter import ttk  #for special effect in tgpa
import re  #for decription of data

# for encription
def change(a):
    a=list(a)
    str=""
    for i in a:
        i=ord(i)
        i=i+1
        i=chr(i)
        str=str+i
    return str

#for dicription
def unchange(a):
    a=list(a)
    st=""
    for i in a:
        i=ord(i)
        i=i-1
        i=chr(i)
        st=st+i
    return st

#for calculating term 1 Tgpa
def tgpa1():
    a=int(a1.get())
    b=int(b1.get())
    c=int(c1.get())
    d=int(d1.get())
    e=int(e1.get())
    f=int(f1.get())
    g=int(g1.get())
    h=int(h1.get())
    i=int(i1.get())
    j=int(j1.get())
    k=int(k1.get())
    l=int(l1.get())
    re1=(a*b)+(c*d)+(e*f)+(g*h)+(i*j)+(k*l)
    xs1=(b+d+f+h+j+l)*9.5
    pres1=re1/xs1
    res1=round(pres1,2)
    if (res1>10):
        dire5.set('10')
    else:
        dire5.set(res1)
    return res1

#for calculating term 2 Tgpa 
def tgpa2():
    a3=int(a2.get())
    b3=int(b2.get())
    c3=int(c2.get())
    d3=int(d2.get())
    e3=int(e2.get())
    f3=int(f2.get())
    g3=int(g2.get())
    h3=int(h2.get())
    i3=int(i2.get())
    j3=int(j2.get())
    k3=int(k2.get())
    l3=int(l2.get())
    re3=(a3*b3)+(c3*d3)+(e3*f3)+(g3*h3)+(i3*j3)+(k3*l3)
    xs3=(b3+d3+f3+h3+j3+l3)*9.5
    pres3=re3/xs3
    res2=round(pres3,2)
    if (res2>10):
        dire4.set('10')
    else:
        dire4.set(res2)
    return res2

#for calculating combined Cgpa,Remark,Grade
def cgpa():
    a=int(a1.get())
    b=int(b1.get())
    c=int(c1.get())
    d=int(d1.get())
    e=int(e1.get())
    f=int(f1.get())
    g=int(g1.get())
    h=int(h1.get())
    i=int(i1.get())
    j=int(j1.get())
    k=int(k1.get())
    l=int(l1.get())
    a3=int(a2.get())
    b3=int(b2.get())
    c3=int(c2.get())
    d3=int(d2.get())
    e3=int(e2.get())
    f3=int(f2.get())
    g3=int(g2.get())
    h3=int(h2.get())
    i3=int(i2.get())
    j3=int(j2.get())
    k3=int(k2.get())
    l3=int(l2.get())
    name = str(name1.get())
    name=change(name)
    
    reg = str(reg1.get())
    reg=change(reg)
    
    re3=(a3*b3)+(c3*d3)+(e3*f3)+(g3*h3)+(i3*j3)+(k3*l3)+(a*b)+(c*d)+(e*f)+(g*h)+(i*j)+(k*l)
    xs3=(b3+d3+f3+h3+j3+l3+b+d+f+h+j+l)*9.5
    pres3=re3/xs3
    res3=round(pres3,2)
    if (res3>10):
        dire.set('10')
    else:    
        dire.set(res3)
    remark=res3
    if(remark<6):
        dire6.set('Need of Improvment  [C]')
    elif(remark>=6 and remark<7):
        dire6.set('Ok but can be Improved  [B]')
    elif(remark>=7 and remark<8):
        dire6.set('Good Keep Going  [B+]')
    elif(remark>=8 and remark<9):
        dire6.set('V.Good Keep Going  [A]')
    elif(remark>=9 and remark<=10):
        dire6.set('Brilliant  [A+]')
    else:
        pass

    #for sending data in Database after encrition
    
    tgpaa=tgpa1()
    tgpab=tgpa2()
    cgpa = res3
    conn = sqlite3.connect('mysql.db')
    with conn:
      cursor = conn.cursor()
      cursor.execute('INSERT INTO result(name, id, tgpa1, tgpa2, cgpa) VALUES(?,?,?,?,?)',(name, reg, tgpaa, tgpab, cgpa))
      db.close()

#for fatching data from Database
      
def search():
    search=str(search1.get())
    search=change(search)
    conn = sqlite3.connect('mysql.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT name FROM result where id ='+search)
    a=cursor.fetchall()
    a=str(a)
    a=unchange(a)  #using decription
    a = " ".join(re.findall("[a-z]+", a))
    pos1.set(a.capitalize())
    
    cursor.execute('SELECT id FROM result where id ='+search)
    b=cursor.fetchall()
    b=str(b)
    b=unchange(b) #using decription
    b = " ".join(re.findall("[0-9]+", b))
    pos2.set(b)
    
    cursor.execute('SELECT tgpa1 FROM result where id ='+search)
    c=cursor.fetchall()
    pos3.set(c)
    
    cursor.execute('SELECT tgpa2 FROM result where id ='+search)
    d=cursor.fetchall()
    pos4.set(d)
    
    cursor.execute('SELECT cgpa FROM result where id ='+search)
    e=cursor.fetchall()
    pos5.set(e)

# To clear all entry field and label for reusing again and again

def reset():
    a1.set("")
    b1.set("")
    c1.set("")
    d1.set("")
    e1.set("")
    f1.set("")
    g1.set("")
    h1.set("")
    i1.set("")
    j1.set("")
    k1.set("")
    l1.set("")
    a2.set("")
    b2.set("")
    c2.set("")
    d2.set("")
    e2.set("")
    f2.set("")
    g2.set("")
    h2.set("")
    i2.set("")
    j2.set("")
    k2.set("")
    l2.set("")
    name1.set("")
    reg1.set("")
    search1.set("")
    pos1.set("")
    pos2.set("")
    pos3.set("")
    pos4.set("")
    pos5.set("")
    dire5.set("")
    dire.set("")
    dire4.set("")
    dire6.set("")
    
win=Tk()
win.geometry("680x750")
win.title('Cgpa Calculator')
win.configure(bg='#F88379')

db = sqlite3.connect('mysql.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS result(name TEXT, id TEXT PRIMARY KEY, tgpa1 REAL, tgpa2 REAL, cgpa REAL)")
db.commit()

# initialising all varables

a1=StringVar()
b1=StringVar()
c1=StringVar()
d1=StringVar()
e1=StringVar()
f1=StringVar()
g1=StringVar()
h1=StringVar()
i1=StringVar()
j1=StringVar()
k1=StringVar()
l1=StringVar()

a2=StringVar()
b2=StringVar()
c2=StringVar()
d2=StringVar()
e2=StringVar()
f2=StringVar()
g2=StringVar()
h2=StringVar()
i2=StringVar()
j2=StringVar()
k2=StringVar()
l2=StringVar()

name1=StringVar()
reg1=StringVar()
search1=StringVar()

pos1 = StringVar()
pos2 = StringVar()
pos3 = StringVar()
pos4 = StringVar()
pos5 = StringVar()

#starting of GUI..................

#part 1 of GUI
lab=Label(win,text="",bg="#F88379") #label
lab.grid(row=1,column=1)
dire=Label(win,text="SEMESTER-1",font="Helvetica 15 bold",bg="#00cca3") #label
dire.grid(row=1,column=6)

dire=Label(win,text="Marks  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=2,column=6)
dire=Label(win,text="Credit  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=2,column=8)


dire=Label(win,text="Subject 1 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=4,column=1)

entry1=Entry(win,textvariable=a1,justify='center') #Entry field
entry1.grid(row=4,column=6)

entry2=Entry(win,textvariable=b1,justify='center') #Entry field
entry2.grid(row=4,column=8)

dire=Label(win,text="Subject 2 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=5,column=1)

entry3=Entry(win,textvariable=c1,justify='center') #Entry field
entry3.grid(row=5,column=6)

entry4=Entry(win,textvariable=d1,justify='center') #Entry field
entry4.grid(row=5,column=8)

dire=Label(win,text="Subject 3 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=6,column=1)

entry5=Entry(win,textvariable=e1,justify='center') #Entry field
entry5.grid(row=6,column=6)

entry6=Entry(win,textvariable=f1,justify='center') #Entry field
entry6.grid(row=6,column=8)

dire=Label(win,text="Subject 4 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=7,column=1)

entry7=Entry(win,textvariable=g1,justify='center') #Entry field
entry7.grid(row=7,column=6)

entry8=Entry(win,textvariable=h1,justify='center') #Entry field
entry8.grid(row=7,column=8)

dire=Label(win,text="Subject 5 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=8,column=1)

entry9=Entry(win,textvariable=i1,justify='center') #Entry field
entry9.grid(row=8,column=6)

entry10=Entry(win,textvariable=j1,justify='center') #Entry field
entry10.grid(row=8,column=8)

dire=Label(win,text="Subject 6 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=9,column=1)

entry11=Entry(win,textvariable=k1,justify='center') #Entry field
entry11.grid(row=9,column=6)

entry12=Entry(win,textvariable=l1,justify='center') #Entry field
entry12.grid(row=9,column=8)

button1=ttk.Button(win,text="Find Tgpa",command=tgpa1) #Button for action
button1.grid(row=6,column=14)

dire5=StringVar()

dire1=Label(win,text="Tgpa1:",bg="#F88379",font="Times 11 bold") #label
dire1.grid(row=8,column=12)
dire1=Label(win,textvariable=dire5,bg="#F88379") #label
dire1.grid(row=8,column=14)


lab=Label(win,text="       ",bg="#F88379") #label
lab.grid(row=10,column=1)
dire=Label(win,text="SEMESTER-2",font="Helvetica 15 bold",bg="#00cca3") #label
dire.grid(row=10,column=6)

dire=Label(win,text="Marks  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=11,column=6)
dire=Label(win,text="Credit  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=11,column=8)

dire=Label(win,text="Subject 1 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=12,column=1)

entry1=Entry(win,textvariable=a2,justify='center') #Entry field
entry1.grid(row=12,column=6)
 
entry2=Entry(win,textvariable=b2,justify='center') #Entry field
entry2.grid(row=12,column=8)

dire=Label(win,text="Subject 2 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=13,column=1)

entry3=Entry(win,textvariable=c2,justify='center') #Entry field
entry3.grid(row=13,column=6)

entry4=Entry(win,textvariable=d2,justify='center') #Entry field
entry4.grid(row=13,column=8)

dire=Label(win,text="Subject 3 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=14,column=1)

entry5=Entry(win,textvariable=e2,justify='center') #Entry field
entry5.grid(row=14,column=6)

entry6=Entry(win,textvariable=f2,justify='center') #Entry field
entry6.grid(row=14,column=8)

dire=Label(win,text="Subject 4 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=15,column=1)

entry7=Entry(win,textvariable=g2,justify='center') #Entry field
entry7.grid(row=15,column=6)

entry8=Entry(win,textvariable=h2,justify='center') #Entry field
entry8.grid(row=15,column=8)

dire=Label(win,text="Subject 5 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=16,column=1)

entry9=Entry(win,textvariable=i2,justify='center') #Entry field
entry9.grid(row=16,column=6)

entry10=Entry(win,textvariable=j2,justify='center') #Entry field
entry10.grid(row=16,column=8)

dire=Label(win,text="Subject 6 :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=17,column=1)

entry11=Entry(win,textvariable=k2,justify='center') #Entry field
entry11.grid(row=17,column=6)

entry12=Entry(win,textvariable=l2,justify='center') #Entry field
entry12.grid(row=17,column=8)

button1=ttk.Button(win,text="Find Tgpa",command=tgpa2) #Button for action
button1.grid(row=14,column=14)

dire4=StringVar()

dire1=Label(win,text="Tgpa2:",bg="#F88379",font="Times 11 bold") #label
dire1.grid(row=16,column=12)
dire1=Label(win,textvariable=dire4,bg="#F88379") #label
dire1.grid(row=16,column=14)

lab=Label(win,text="       ",bg="#F88379") #label
lab.grid(row=18,column=6)

dire=Label(win,text="Name :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=19,column=1)

entry14=Entry(win,textvariable=name1,justify='center') #Entry field
entry14.grid(row=19,column=6)

dire=Label(win,text="Reg No :  ",bg="#F88379",font="Times 11 bold") #label
dire.grid(row=21,column=1)

entry15=Entry(win,textvariable=reg1,justify='center') #Entry field
entry15.grid(row=21,column=6)

lab=Label(win,text="       ",bg="#F88379") #label
lab.grid(row=22,column=6)

button1=ttk.Button(win,text="Find cgpa",width=10,command=cgpa) #Button for action
button1.grid(row=23,column=4)

dire=StringVar()

dire1=Label(win,text="Cgpa : ",bg="#F88379",font="Times 11 bold") #label
dire1.grid(row=23,column=6)
dire1=Label(win,textvariable=dire,bg="#F88379") #label
dire1.grid(row=23,column=8)

dire6=StringVar()

dire1=Label(win,text="Remark : ",bg="#F88379",font="Times 11 bold") #label
dire1.grid(row=25,column=4)
dire1=Label(win,textvariable=dire6,bg="#F88379") #label
dire1.grid(row=25,column=6)

lab=Label(win,text="       ",bg="#F88379") #label
lab.grid(row=26,column=6)

#part 2 of GUI

button_reset=ttk.Button(win,text="Reset All The Data",width=20,command=reset) #Button for action
button_reset.grid(row=27,column=6)

lab=Label(win,text="       ",bg="#F88379") #label
lab.grid(row=28,column=6)


entry14=Entry(win,textvariable=search1,justify='center') #Entry field
entry14.grid(row=29,column=6)

button1=ttk.Button(win,text="Search",width=10,command = search) #Button for action
button1.grid(row=29,column=7)

pos6 = Label(win,text = "Name:",bg="#F88379",font="Times 11 bold") #label
pos6.grid(row=30,column=1)
pos6=Label(win,textvariable=pos1,bg="#F88379") #label
pos6.grid(row=30,column=6)

pos7 = Label(win,text = "Id:",bg="#F88379",font="Times 11 bold") #label
pos7.grid(row=31,column=1)
pos7=Label(win,textvariable=pos2,bg="#F88379") #label
pos7.grid(row=31,column=6)

pos8 = Label(win,text = "Tgpa1:",bg="#F88379",font="Times 11 bold") #label
pos8.grid(row=32,column=1)
pos8=Label(win,textvariable=pos3,bg="#F88379") #label
pos8.grid(row=32,column=6)

pos9 = Label(win,text = "Tgpa2:",bg="#F88379",font="Times 11 bold") #label
pos9.grid(row=33,column=1)
pos9=Label(win,textvariable=pos4,bg="#F88379") #label
pos9.grid(row=33,column=6)

pos10 = Label(win,text = "Cgpa:",bg="#F88379",font="Times 11 bold") #label
pos10.grid(row=34,column=1)
pos10=Label(win,textvariable=pos5,bg="#F88379") #label
pos10.grid(row=34,column=6)  

win.mainloop()

# end of GUI