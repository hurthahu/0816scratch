from tkinter import *
from neededFunction import *
import socket
import threading
import tkinter.messagebox
import tkinter
li=[]
def teaview():
    teawin=Tk()
    teawin.title("教师系统")
    teawin.geometry("430x320")
    v1=StringVar()
    v1.set("欢迎进入教师端考试系统")
    lable=Label(teawin,bg="#44ffff",font=("楷体",20),textvariable=v1)
    lable.place(x=0,width=430,y=0,height=80)
    def pick():
        xuanren()

    def check():


        for ss in li:
            ss.send("收作业".encode("utf8"))

    Inbut=Button(teawin,bg="yellow",text="导入题目")
    Inbut.place(x=100,width=100,y=150,height=40)
    checkbut=Button(teawin,bg="yellow",text="收作业",command=check)
    checkbut.place(x=230,width=100,y=150,height=40)
    pickbut=Button(teawin,bg="yellow",text="随机点名",command=pick)
    pickbut.place(x=100,width=100,y=210,height=40)
    selectbut=Button(teawin,bg="yellow",text="查询信息")
    selectbut.place(y=210,height=40,x=230,width=100,)
    selectbut = Button(teawin, bg="yellow", text="在线考试",command=start)
    selectbut.place(y=270, height=40, x=230, width=100, )

    teawin.mainloop()
def teaServer():
    ser = socket.socket()
    ser.bind(('192.168.43.177', 7777))
    ser.listen(20)
    while True:
        s, add = ser.accept()
        li.append(s)
        info1=s.recv(1024)
        messagebox.showinfo("",info1)
# slist=[]
def start():
    tkinter.messagebox.showinfo("连接成功","请学生开始连接准备考试")
    for ss in li:
        ss.send("start".encode("utf-8"))
        # app.destroy()


# def teachermain():
#     app=tkinter.Tk()
#     b=tkinter.Button(app,text="开始考试",command=lambda :start(app))
#     b.place(x=20,y=20,height=100,width=100)
#     app.mainloop()


def startThread():
    if __name__!="__main__":
        # threading.Thread(target=teachermain).start()
        threading.Thread(target=teaview,args=()).start()
        threading.Thread(target=teaServer,args=()).start()

