import psutil as pt


class CpuBar:
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)  # количество ядер
        self.cpu_count_logical = pt.cpu_count()  # количество процессов

    def cpu_percent_return(self):
        """Возвращает загрузку процессов"""
        return pt.cpu_percent(percpu=True)

    def cpu_one_return(self):
        """Возвращает суммарную загрузку процессора"""
        return pt.cpu_percent()

    def ram_usage(self):
        """Возвращает загрузку оперативной памяти"""
        return pt.virtual_memory()

