# TODO написать функцию remove
def remove(target: list, value: int) -> list:
    last_index = None
    for index, list_value in enumerate(target):
        if list_value == value:
            last_index = index

    if last_index is None:
        raise ValueError("Нет значения")
    else:
        return target[:last_index] + target[last_index + 1:]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
