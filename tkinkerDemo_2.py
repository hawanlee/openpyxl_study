#! /usr/bin/python
# coding=utf-8

import tkinter as tk

class App:
    def __init__ (self, root):
        # 创建一个框架，然后在里面添加一个Button组件
        # 框架一般用于在复杂的布局中起到组件分组的作用
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame, text='say hi', command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print('hello everyone')

root=tk.Tk()
app=App(root)

root.mainloop()