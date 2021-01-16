# from DB.localDB import LocalDB
import tkinter as tk
from table import Table

root = tk.Tk()

root.title("Table Test")
root.minsize(100, root.winfo_screenheight() // 2)
root.maxsize(root.winfo_screenwidth(), int(root.winfo_screenheight() * 0.9))

rs = [[i, f'test{i}', f'88003{i}0{i}', 'else'] for i in range(1, 50)]

table = Table(root, headings=['id', 'username', 'phone', 'something'], rows=rs, font_size=12)
table.pack(pady=5, padx=20)
table.draw_table()

root.mainloop()
