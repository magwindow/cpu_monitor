class ConfigureWidgets:
    def configure_cpu_bar(self):
        r = self.cpu.cpu_percent_return()  # список с процентами загрузки
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i + 1} usage: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAM Занято: {r2[2]}%\nИспользуется: {round(r2[3] / 1048576)} Mb,\
                  \nСвободно: {round(r2[1] / 1048576)} Mb')
        self.ram_bar.configure(value=r2[2])

        self.wheel = self.after(1000, self.configure_cpu_bar)  # обновление прогресс бара в 1 сек

    def configure_win(self):
        """Добавляет, убирает рамку при нажатии на кнопку 'Обновить'"""
        if self.wm_overrideredirect():  # если окно с рамкой
            self.overrideredirect(False)  # убираем рамку
        else:
            self.overrideredirect(True)  # ставим рамку
        self.update()  # обновляет содержимое окна

    def clear_win(self):
        """Очищает все виджеты с окна"""
        for i in self.winfo_children():
            i.destroy()  # убираем все виджеты с окна
