#! /usr/bin/python
# coding=utf-8

from tkinter import *

# 所谓布局，就是指控制窗体容器中各个控件（组件）的位置关系。tkinter 共有三种几何布局管理器，分别是：pack布局，grid布局，place布局。

class App:
    def __init__(self, master):
        #使用Frame增加一层容器
        fm1 = Frame(master)
        #Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Button(fm1, text='Top').pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm1, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm1, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        Button(fm2, text='Left').pack(side=LEFT)
        Button(fm2, text='This is the Center button').pack(side=LEFT)
        Button(fm2, text='Right').pack(side=LEFT)        
        fm2.pack(side=LEFT, padx=10)


root = Tk()
root.title("Pack - Example")
display = App(root)
root.mainloop()