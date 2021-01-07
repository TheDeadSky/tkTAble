# from DB.localDB import LocalDB
import tkinter as tk
from table import Table

root = tk.Tk()

root.title("Table Test")
root.minsize(100, root.winfo_screenheight() // 2)

table = Table(root, headings=['id', 'username', 'phone'], rows=[[1, 'avon', '88003600'],
                                                                [2, 'test1', '123213213'],
                                                                [3, 'test2', '099875453']], font_size=12)
table.pack(pady=5, padx=20)
table.draw_table()

root.mainloop()
