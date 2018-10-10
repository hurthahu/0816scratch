import os
import pymysql
from tkinter import  *
import socket
from  neededFunction import *
from  学生界面 import  *
from 教师界面 import  startThread
win=Tk()
win.geometry("430x320")
v1=StringVar()
v2=StringVar()

def StuVerify():
    stuid=entry1.get()
    stuname=entry2.get()
    num=stuv(stuid,stuname)
    if num==1:
        win.destroy()
        Start(stuid)

def TeaVerify():
    teaid=entry1.get()
    teaname=entry2.get()
    num=teav(teaid,teaname)
    if num==1:
        win.destroy()
        startThread()

lable=Label(win,bg="#44ffff",text="欢迎进入教务系统",font=("楷体",30))
lable.place(x=0,y=0,width=430,height=80)
entry1=Entry(win,textvariable=v1)
entry1.place(x=120,y=100,height=35,width=210)
entry2=Entry(win,textvariable=v2)
entry2.place(x=120,y=150,height=35,width=210)
but=Button(win,text="学生登录",font=("黑体",11),bg="#1FC7FD",command=StuVerify)
but.place(x=130,y=210,height=35,width=90)
but=Button(win,text="教师登录",font=("黑体",11),bg="#1FC7FD",command=TeaVerify)
but.place(x=230,y=210,height=35,width=90)

win.mainloop()