import pymysql
from tkinter import messagebox
import socket
from tkinter import  filedialog
import time
conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="admin123456", database="tiku", charset="utf8")
cur=conn.cursor()

def xuanren():
    import pymysql
    from random import choice
    import tkinter.messagebox

    conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="admin123456", database="test1", charset="utf8")
    cur=conn.cursor()
    list2=[]
    sql="select stuName from stuinfo"
    cur.execute(sql)
    list1=cur.fetchall()
    for i in list1:
        list2.append(i)
    aa=choice(list2)
    bb=list(aa)
    tkinter.messagebox.showinfo("恭喜",bb[0])
def stuv(stuid,stuname):
    li2=[]
    con=pymysql.connect(host="localhost",port=3306,user="root",
    password="admin123456",database="tiku",charset="utf8")

    cur=con.cursor()
    sql="select stuId,stuName from stuinfo"
    cur.execute(sql)
    stuinfo=list(cur.fetchall())
    for i in stuinfo:
        j=list(i)
        li2.append(j)
    if [stuid,stuname] in li2:
        messagebox.showinfo("提示","登录成功")
        return  1
    else:
        messagebox.showerror("错误", "学号或密码错误")
        return 2
def teav(teaid,teaname):
    li2=[]
    con=pymysql.connect(host="localhost",port=3306,user="root",
    password="admin123456",database="tiku",charset="utf8")

    cur=con.cursor()
    sql="select teaId,teaName from teainfo"
    cur.execute(sql)
    stuinfo=list(cur.fetchall())
    for i in stuinfo:
        j=list(i)
        li2.append(j)
    if [teaid,teaname] in li2:
        messagebox.showinfo("提示","登录成功")
        return 1
    else:
        messagebox.showerror("错误","学号或密码错误")
        return 2
def qiandao(stuid):
    li=[]
    tm = time.ctime().split(":")
    tm = tm[0] + ":" + tm[1]
    ip = socket.gethostbyname(socket.gethostname())
    tmip1=tm+ip
    sql="select tmip from score where stuId=%s"
    cur.execute(sql,stuid)
    m=cur.fetchone()[0]
    print(m)
    if tmip1==m:
        messagebox.showerror("","签到过了")
    else:
        sql2="update score set tmip = %s where stuId=%s"
        cur.execute(sql2,(tmip1,stuid))
        conn.commit()
        messagebox.showinfo("","签到成功")


    # sql="update score set performance=performance +5 where stuid=%s"
    # cur.execute(sql,(stuid,))
    # conn.commit()
    # messagebox.showinfo("恭喜","签到成功")
def jiaozuoye():
    name=filedialog.askopenfilename()
    file1=open(name,"rb")
    file=file1.read()
    file1.close()




