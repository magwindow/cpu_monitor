import psutil as pt


class CpuBar:
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        print(f'Количество ядер процессора: {self.cpu_count}')


CpuBar()