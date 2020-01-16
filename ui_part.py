import tkinter
import get_words_frequency as gwf



win = tkinter.Tk()
win.title("Python-14")
win.geometry("500x500+200+100")
# 创建一个输入框
entry = tkinter.Text(win)
entry.pack()


# 写一个读取文件的函数
def func():
    gwf.essay_content = 123 = entry.get(0.0, tkinter.END)
    text.insert(tkinter.INSERT, content)


button = tkinter.Button(win, text="filter", command=func)
button.pack()

# 创建一个文本框
text = tkinter.Text(win)
text.pack()
win.mainloop()
