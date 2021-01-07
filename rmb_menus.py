##################################################
# В этом файле хранятся меню правой кнопки мыши #
##################################################
import tkinter as tk
import sys
import subprocess


def copy_to_clipboard(data_to_copy):
    if sys.platform.startswith('win32'):
        po = subprocess.Popen(f'echo {data_to_copy}|clip',
                              stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    elif sys.platform.startswith('linux'):
        po = subprocess.Popen(f'echo {data_to_copy}|xclip -selection clipboard',
                              stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    elif sys.platform.startswith('darwin'):
        po = subprocess.Popen(f'echo {data_to_copy}|pbcopy',
                              stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    else:
        raise Exception(f"Unsupported OS platform: '{sys.platform}'")


class RowMenu(tk.Menu):
    """Меню для каждой строки таблицы"""

    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.add_command(label="Копировать колонку", command=self.copy_to_cb_action)
        self.add_command(label="Копировать всю строку", command=self.copy_row_to_cb_action)
        self.add_separator()
        self.add_command(label="Редактировать")
        self.add_command(label="Удалить")

        self.current_widget = None

    def make_popup(self, event):
        try:
            self.current_widget = event.widget
            self.tk_popup(event.x_root, event.y_root)
        finally:
            self.grab_release()

    def copy_to_cb_action(self):
        copy_to_clipboard(self.current_widget.get())
        self.grab_release()

    def copy_row_to_cb_action(self):
        current_row_name = self.current_widget.winfo_name()[:2]
        row = {k: v for k, v in self.current_widget.master.children.items() if k.startswith(current_row_name)}
        txt_row = [i.get() for i in row.values()]
        copy_to_clipboard(", ".join(txt_row))
        self.grab_release()
