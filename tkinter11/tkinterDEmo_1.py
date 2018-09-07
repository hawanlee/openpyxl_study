#! /usr/bin/python
# coding=utf-8

import tkinter as tk

# 不要把文件名写成库的名字！！！！！！！

root=tk.Tk()
root.title('Demo interface')
theLabel=tk.Label(root,text='我的一个窗口程序')
theLabel.pack()
root.mainloop()
