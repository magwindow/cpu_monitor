import psutil as pt


class CpuBar:
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)  # количество ядер
        self.cpu_count_logical = pt.cpu_count()  # количество процессов

    def cpu_percent_return(self):
        """Возвращает загрузку процессов"""
        return pt.cpu_percent(percpu=True)


x = CpuBar()

for _ in range(10):
    print(x.cpu_percent_return())



