import socket
import pymysql
import tkinter
from tkinter import *
import tkinter.messagebox

list1=[]
list2=[]
s=socket.socket()
s.connect(('192.168.10.109',8888))
mess=s.recv(1024).decode("utf-8")
if mess=="start":
    fd = tkinter.Tk()
    fd.geometry("900x900")
    coon = pymysql.connect(host="localhost", port=3306,
                           user="root", password="admin123456",
                           database="tiku", charset="utf8")
    cur = coon.cursor()
    i = 1
    m = 0
    count = 0
    def check():
        global i
        global count
        global m
        sql = "select ios from timu2"
        row = cur.execute(sql)
        if row == count:
            var1.set("题目已经做完了")
            tkinter.messagebox.showerror("错误", "题目已经出完了")
            return
        else:
            sql = "select * from timu2 WHERE ios=%s"#顺序出题
            cur.execute(sql, (i))
            add = cur.fetchone()
            if add[2] not in list2:
                list2.append(add[2])
                list1.append(add[1])
                m += 1
                var1.set(add[2] + "\n" + add[3] + "\n" + add[4] + "\n" + add[5] + "\n" + add[6])
                count += 1
                i += 1
            else:
                check()
    def get():
        commm = var3.get()
        var2.set("您的选择是：" + commm)
    def xxx(m):
        cnnn = var3.get()
        if str(cnnn) == list1[m - 1]:
            var2.set("回答正确")
            sql1="update mark set mark=mark+5 WHERE id=1001"
            cur.execute(sql1)
            coon.commit()
        else:
            var2.set("回答错误")
    def exite():
        fd.destroy()
    var1 = StringVar()
    var1.set("点击下一题考试")
    var2 = StringVar()
    var3 = StringVar()
    var3.set("a")
    label = tkinter.Label(fd, textvariable=var1, bg="#44ffff", font=("Arial", 12))
    label.place(x=0, y=0, height=300, width=700)
    label = tkinter.Label(fd, textvariable=var2, bg="red", font=("Arial", 12))
    label.place(x=700, y=0, height=300, width=200)
    button1 = tkinter.Radiobutton(fd, text="A", value="A", variable=var3, bg="white", command=get)
    button1.place(x=400, y=400, height=30, width=100)
    button2 = tkinter.Radiobutton(fd, text="B", value="B", variable=var3, bg="white", command=get)
    button2.place(x=400, y=450, height=30, width=100)
    button3 = tkinter.Radiobutton(fd, text="C", value="C", variable=var3, bg="white", command=get)
    button3.place(x=400, y=500, height=30, width=100)
    button4 = tkinter.Radiobutton(fd, text="D", value="D", variable=var3, bg="white", command=get)
    button4.place(x=400, y=550, height=30, width=100)
    button5 = tkinter.Button(fd, text="下一题", bg="white", command=check)
    button5.place(x=0, y=330, height=60, width=150)  # 随机选题
    button6 = tkinter.Button(fd, text="判断对错", bg="white", command=lambda: xxx(m))
    button6.place(x=0, y=420, height=60, width=150)
    button7 = tkinter.Button(fd, text="退出", bg="white", command=exite)
    button7.place(x=0, y=510, height=60, width=150)
    fd.mainloop()