# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary():
    name, hour, rate, bonus = argv
    zp = (int(hour) * int(rate)) + int(bonus)
    print(f"Расчёта заработной платы: {zp}")