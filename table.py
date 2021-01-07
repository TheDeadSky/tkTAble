import tkinter as tk

from rmb_menus import RowMenu
from tolltip import ToolTip

# Entry states:
NORMAL = 'normal'
READONLY = 'readonly'
DISABLED = 'disabled'


class Table(tk.Frame):
    def __init__(self, master, headings: list = None, rows: list = None, font_size=9, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.font_size = font_size
        if headings is None:
            headings = []

        if rows is None:
            rows = []

        self.table = {
            "headings": headings,
            "rows": rows
        }

        self.headings = []
        self.rows = []

        self.last_row = 0

        print(self.table)
        print(self.headings)

    def create_from_dict(self, table: dict):
        pass

    def create_empty(self):
        return self.table['headings']

    def draw_table(self):
        self.headings.clear()
        self.rows.clear()

        self.draw_headings()
        self.draw_rows()

    def draw_headings(self):
        col = 0

        for h in self.table['headings']:
            head = tk.Button(self, text=h, font=('Helvetica', self.font_size, 'bold'),
                             borderwidth=2, relief="solid", padx=10, pady=5)
            self.headings.append(head)
            head.grid(row=self.last_row, column=col, sticky=tk.W + tk.E)
            col += 1

        self.last_row += 1

    def draw_row(self, data: list):
        col = 0
        rmb_popup_menu = RowMenu(self.master, tearoff=0)

        for d in data:
            str_var = tk.StringVar(name=f"r{self.last_row+1}{self.table['headings'][col]}", value=d)

            row_column = tk.Entry(self, text=str_var, font=('Helvetica', self.font_size),
                                  borderwidth=1, relief="solid", width=10, state=READONLY,
                                  name=f'r{self.last_row + 1}c{col}')

            tt = ToolTip(row_column, str_var.get())

            row_column.bind('<Button-3>', rmb_popup_menu.make_popup)

            row_column.grid(row=self.last_row, column=col, sticky=tk.W + tk.E)
            self.rows.append(row_column)
            col += 1

        self.last_row += 1

    def draw_rows(self):
        for row_data in self.table['rows']:
            self.draw_row(row_data)

    def add_row(self, data: list):
        self.table['rows'].append(data)
