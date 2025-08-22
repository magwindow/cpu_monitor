import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)  # непрозрачность 100%
        self.attributes('-topmost', True)  # расположить поверх окон
        self.overrideredirect(True)  # убирает рамки
        self.resizable(False, False)
        self.title('CPU-RAM')


if __name__ == '__main__':
    root = Application()
    root.mainloop()
