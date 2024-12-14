import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from PIL import Image
import  random
#https://customtkinter.tomschimansky.com/documentation/widgets/button
def lr():
    global stu
    stu = ["张三","李四","王五"]
    列表.delete(0,tk.END)
    名字.configure(text=' ')
def choice():
    a = random.choice(stu)
    列表.insert(tk.END,a)
    名字.configure(text=a)
def choice_3():
    列表.delete(0,tk.END)
    for i in range(3):
        choice()
        名字.configure(text='看列表')
def choice_5():
    列表.delete(0,tk.END)
    for i in range(5):
        choice()
        名字.configure(text='看列表')      
def get_img(filename, width, height):
    im = Image.open(filename).resize((width, height))
    im = ImageTk.PhotoImage(im)
    return im
def rest():
    tk.messagebox.showinfo('你好','是这样的')
    pass

# tk 窗口基本配置
r = ctk.CTk()
r.title('命运抉择 2.0')
r.geometry('600x500')
ctk.set_appearance_mode("light")
r.resizable(width=False,height=False)

#计算屏幕中央的位置
x = int((r.winfo_screenwidth() - r.winfo_reqwidth()) / 3)
y = int((r.winfo_screenheight() - r.winfo_reqheight()) / 3)
#将窗口居中显示
r.geometry("+{}+{}".format(x, y))

# 设置背景图片
背景 = ctk.CTkCanvas(r, width=1000, height=600)
图片 = get_img('./background.jpg', 1000, 600)
背景.create_image(340, 200, image=图片)
背景.place(x=0,y=0)

# 控件配置
文字 = ctk.CTkLabel(r,text='被抽取到的幸运儿是:',font=('站酷文艺体',28),fg_color="transparent",bg_color="transparent")
名字 = ctk.CTkLabel(r,font=('微软雅黑',28),text_color='black',text='')
滚动条 = ctk.CTkScrollbar(r)
列表 = tk.Listbox(r,width=23)
单抽 = ctk.CTkButton(r,fg_color='pink',hover_color='#e6adb7',text='来一发?',command=choice,width=12,text_color='black',font=('微软雅黑',20))
一键三连 = ctk.CTkButton(r,fg_color='pink',hover_color='#e6adb7',text='一键三连',command=choice_3,width=12,text_color='black',font=('微软雅黑',20))
重置=ctk.CTkButton(r,fg_color='pink',hover_color='#e6adb7',command=rest,text='重置',width=12,text_color='black',font=('微软雅黑',20))
五连绝世=ctk.CTkButton(r,fg_color='pink',hover_color='#e6adb7',text='五连抽',command=choice_5,width=12,text_color='black',font=('微软雅黑',20))

#DLC:滚动条与列表的禁忌之恋
列表.config(yscrollcommand=滚动条.set)
滚动条.configure(command=列表.yview)

# 控件位置
文字.grid(column=1,row=0)
名字.grid(column=2,row=0)
列表.grid(column=1, row=1)
滚动条.grid(column=0, row=1, sticky='ns')
#单抽.grid(column=2,row=1)
单抽.place(x=280,y=120)
#一键三连.grid(column=3,row=1)
一键三连.place(x=400,y=120)
#五连绝世.grid(column=2,row=2)
五连绝世.place(x=280,y=200)
#重置.grid(column=1,row=3)
重置.place(x=120,y=260)

#菜单栏
lst=tk.Menu(r)
lst.add_command()

#提供列表
lr()

#测试区


#dddd
r.mainloop()

