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

        self.bar2 = ttk.LabelFrame(self, text='Панель мониторинга CPU-RAM')
        self.bar2.pack(fill=tk.X)

        # выпадающий список
        self.combo_win = ttk.Combobox(self.bar2, values=["Скрывать", "Не скрывать", "Свернуть"],
                                      state='readonly', width=12)
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)

        # кнопки "Обновить" и ">>>"
        ttk.Button(self.bar2, text='Обновить').pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar = ttk.LabelFrame(self, text='Мощность')
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def app_exit(self):
        """Метод класса, который выходит из приложения при нажатии на кнопку 'Выход'"""
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Application()
    root.mainloop()
