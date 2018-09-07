#! /usr/bin/python
# coding=utf-8

import tkinter as tk

class App:
    def __init__ (self, root):
        # 创建一个框架，然后在里面添加一个Button组件
        # 框架一般用于在复杂的布局中起到组件分组的作用
        frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        # 创建一个按钮组件，fg是前景色的缩写
        self.hi_there = tk.Button(frame, text='say hi',fg='blue', bg='green', command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print('hello everyone')

# 创建一个toplevel的根窗口，并把它作为参数实例化app对象
root=tk.Tk()
app=App(root)
# 开始事件主循环
root.mainloop()