from tkinter import *
from tkcalendar import DateEntry

root = Tk()
root.geometry("300x200")

# 日期选择组件
cal = DateEntry(root, width=12, background='darkblue',
                foreground='white', borderwidth=2,
                date_pattern='yyyy-mm-dd')
cal.pack(pady=20)

# 获取选中的日期
def get_date():
    print(cal.get_date())  # 返回 datetime.date 对象

Button(root, text="获取日期", command=get_date).pack()

root.mainloop()