import socket
import tkinter

import threading

slist=[]
def start(app):
    for ss in slist:
        ss.send("start".encode("utf-8"))
        app.destroy()


def teachermain():
    app=tkinter.Tk()
    b=tkinter.Button(app,text="开始考试",command=lambda :start(app))
    b.place(x=20,y=20,height=100,width=100)
    app.mainloop()


def teacherlisten():
    server=socket.socket()
    server.bind(('192.168.10.109',8888))
    server.listen(100)
    while True:
        s,addr=server.accept()
        slist.append(s)


if __name__=="__main__":
    threading.Thread(target=teachermain).start()
    threading.Thread(target=teacherlisten).start()

