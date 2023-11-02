# TODO написать функцию index
import typing


def index(items, value_to_search):
    list_index = [index for index, value in enumerate(items) if value == value_to_search]
    if not list_index: raise ValueError("Значение не найдено")

    return list_index


if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
