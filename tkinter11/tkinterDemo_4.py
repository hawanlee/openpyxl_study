from tkinter import *

#创建根窗口
root = Tk()
#设置窗口标题
root.title("Hello")
#设置窗口大小
root.geometry("300x200")
#在窗体中创建一个框架，用它来承载其他小部件
app = Frame(root)
#设置布局管理器
app.grid()

label = Label(app,text="hello word!")
label.grid()

btn = Button(app)
btn.grid()

#小部件的任何选项都可以通过configure()方法操作
btn.configure(text = "click")

root.mainloop();