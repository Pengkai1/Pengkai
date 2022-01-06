from tkinter import *
import os
from PIL import Image as imageaaa
from collections import Counter
from tkinter import *


def myLabel():
    url = "source/"
    saveurl = "target/"

    for i in os.listdir(url):
        bei = name.get()
        if bei == "0":
            pass
        else:
            bei = name.get().split("，")
            bei = (int(bei[0]), int(bei[1]), int(bei[2]))
        bian = name1.get().split("，")
        bian = (int(bian[0]), int(bian[1]), int(bian[2]))
        im = imageaaa.open(os.path.join(url, i))
        width = im.size[0]  # 获取宽度
        height = im.size[1]  # 获取长度
        if bei == "0":
            bei = Counter([im.getpixel((0, 0,)), im.getpixel((width - 1, 0,)), im.getpixel((0, height - 1,)),
                           im.getpixel((width - 1, height - 1,))]).most_common(1)[0][0]
        for x in range(width):
            for y in range(height):
                rgb = im.getpixel((x, y,))
                if sum(bei) > sum(rgb):
                    if rgb == bei or bei[0] - rgb[0] < 20 and bei[1] - rgb[1] < 20:
                        im.putpixel((x, y), bian)
                else:
                    if rgb == bei or rgb[0] < bei[0] + 70 and rgb[1] < bei[1] + 50:
                        im.putpixel((x, y), bian)
        im.save(os.path.join(saveurl, i))
    Label(monty, text="Successful", bg="pink").pack()
html = Tk()
html.geometry("500x200")
monty = LabelFrame(html, bg="pink", text=" Change_colour ")     # 创建一个容器，其父容器为html
monty.grid(column=0, row=0, padx=10, pady=10)       # padx  pady   该容器外围需要留出的空余空间
aLabel = Label(monty, text="A Label")
div=Frame(monty,bg="pink")
div["width"]=475
div["height"]=0
div.pack()
Label(monty,text="source:",bg="pink").pack()
name = StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = Entry(monty, width=50, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
#nameEntered.grid(column=0, row=1, sticky=W)       # 设置其在界面中出现的位置  column代表列   row 代表行
nameEntered.focus()     # 当程序运行时,光标默认会出现在该文本框中
nameEntered.pack()
Label(monty,text="target:",bg="pink").pack()
name1 = StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
name1Entered = Entry(monty, width=50, textvariable=name1)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
#nameEntered.grid(column=0, row=1, sticky=W)       # 设置其在界面中出现的位置  column代表列   row 代表行
name1Entered.pack()
div=Frame(monty,bg="pink")
div["width"]=475
div["height"]=10
div.pack()
Button(monty,bg="pink", text=" Change ",command=myLabel).pack()
div=Frame(monty,bg="pink")
div["width"]=475
div["height"]=10
div.pack()
html.mainloop()
