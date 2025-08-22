import psutil as pt


class CpuBar:
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()
        print(f'Количество ядер процессора: {self.cpu_count}')
        print(f'Количество потоков: {self.cpu_count_logical}')


CpuBar()