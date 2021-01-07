##################################################
# В этом файле хранятся меню правой кнопки мыши #
##################################################
import tkinter as tk
import sys
import subprocess


def copy_to_clipboard(data_to_copy):
    if sys.platform.startswith('win32'):
        po = subprocess.Popen(f'echo {repr(data_to_copy)}|clip', stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    elif sys.platform.startswith('linux'):
        po = subprocess.Popen(f'echo {repr(data_to_copy)}|xclip -selection clipboard', stdout=subprocess.PIPE, shell=True)
    elif sys.platform.startswith('darwin'):
        pass
    else:
        raise Exception(f"Unsupported OS platform: '{sys.platform}'")


class RowMenu(tk.Menu):
    """Меню для каждой строки таблицы"""

    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.add_command(label="Копировать колонку", command=lambda: self.copy_to_clipboard_action(self.current_widget.get()))
        self.add_command(label="Копировать всю строку")
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


    def copy_to_clipboard_action(self, text):
        copy_to_clipboard(text)
        print("???")
        self.grab_release()