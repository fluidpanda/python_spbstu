# TODO Распечатать таблицу умножения
from icecream import ic

array: list = []

for a in range(2, 10):
    for b in range(2, 10):
        result = a * b
        end = " " if b != 9 else ""
        print(f"{result:2}", end=end)
    print()
