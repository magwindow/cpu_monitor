import sys
import tkinter as tk
from tkinter import ttk
from process import CpuBar
from widget_update import ConfigureWidgets


class Application(tk.Tk, ConfigureWidgets):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)  # непрозрачность 100%
        self.attributes('-topmost', True)  # расположить поверх окон
        self.overrideredirect(True)  # убирает рамки
        self.resizable(False, False)
        self.title('CPU-RAM')

        # вызов класса из модуля process.py
        self.cpu = CpuBar()

        # вызов метода
        self.run_set_ui()

    def run_set_ui(self):
        # вызов методов класса Application
        self.set_ui()
        self.make_bar_cpu_usage()
        # вызов метода, унаследованного ConfigureWidgets из модуля widget_update.py
        self.configure_cpu_bar()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Выход', command=self.app_exit)
        exit_but.pack(fill=tk.X)

        self.bar2 = ttk.LabelFrame(self, text='Панель мониторинга CPU-RAM')
        self.bar2.pack(fill=tk.X)

        # выпадающий список
        self.combo_win = ttk.Combobox(self.bar2, values=["Скрывать", "Не скрывать", "Мин.режим"],
                                      state='readonly', width=12)
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)

        # кнопки "Обновить" и ">>>"
        ttk.Button(self.bar2, text='Обновить', command=self.configure_win).pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar = ttk.LabelFrame(self, text='Мощность')
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.combo_win.bind('<<ComboboxSelected>>', self.choise_combo)

    def make_bar_cpu_usage(self):
        """Показывает сколько ядер и процессов"""
        ttk.Label(self.bar, text=f'Physical cores: {self.cpu.cpu_count}, Logical cores: {self.cpu.cpu_count_logical}',
                  anchor=tk.CENTER).pack(fill=tk.X)

        # в списках хранятся метки и прогресс бары
        self.list_label = []
        self.list_pbar = []

        for _ in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar, length=100))

        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)

    def make_minimal_win(self):
        # прогресс бар для загрузки процессора
        self.bar_one = ttk.Progressbar(self, length=100)
        self.bar_one.pack(side=tk.LEFT)

        # прогресс бар для загрузки оперативной памяти
        self.ram_bar = ttk.Progressbar(self, length=100)
        self.ram_bar.pack(side=tk.LEFT)

        # кнопки полного режима и перемещения
        ttk.Button(self, text='Полный режим', command=self.make_full_win, width=15).pack(side=tk.RIGHT)
        ttk.Button(self, text='Переместить', command=self.configure_win, width=15).pack(side=tk.RIGHT)

        self.update()
        self.configure_minimal_win()

    def enter_mouse(self, event):
        """Срабатывает при на ведение курсора мыши на виджет"""
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        """Срабатывает убирание курсора мыши с виджета"""
        if self.combo_win.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def choise_combo(self, event):
        if self.combo_win.current() == 2:
            self.enter_mouse('')
            self.unbind_class('Tk', '<Enter>')  # отвязываем событие на ведение курсора мыши
            self.unbind_class('Tk', '<Leave>')  # отвязываем событие убирание курсора мыши
            self.combo_win.unbind('<<ComboboxSelected>>')  # отвязываем событие ComboboxSelected
            self.after_cancel(self.wheel)  # прерывание процесса обновления self.wheel
            self.clear_win()  # вызов метода класса ConfigureWidgets
            self.update()  # обновляем окно
            self.make_minimal_win()  # вызов метода, который прорисовывает новые виджеты

    def make_full_win(self):
        self.after_cancel(self.wheel)
        self.clear_win()
        self.update()
        self.run_set_ui()
        self.enter_mouse('')
        self.combo_win.current(1)

    def app_exit(self):
        """Метод класса, который выходит из приложения при нажатии на кнопку 'Выход'"""
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Application()
    root.mainloop()
