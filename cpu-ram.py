import sys
import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)  # непрозрачность 100%
        self.attributes('-topmost', True)  # расположить поверх окон
        self.overrideredirect(True)  # убирает рамки
        self.resizable(False, False)
        self.title('CPU-RAM')

        self.set_ui()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Выход', command=self.app_exit)
        exit_but.pack(fill=tk.X)

    def app_exit(self):
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Application()
    root.mainloop()
