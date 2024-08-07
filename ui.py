import tkinter as tk

from generator import generate


top = tk.Tk()
top.geometry('500x250')
top.title("随机密码生成器")

# 添加标签控件
label = tk.Label(top,text="密码长度",font=("宋体",25))
# 定位
label.grid(row=0,column=0)

# 添加输入框
entry = tk.Entry(top)
entry.grid(row=0,column=1)

def func():
    s = int(entry.get())
    r = generate(s)
    print(r)

    t.insert("insert",r)

    return r


# 按钮
button = tk.Button(top,text="生成",font=("宋体",25),fg="red",command=func)
button.grid(row=1,column=1)

t = tk.Text(top , height=1, width=15)
t.grid(row=2,column=1)

top.mainloop()




