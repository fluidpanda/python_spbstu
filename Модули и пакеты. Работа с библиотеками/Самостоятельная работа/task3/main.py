import random


def get_unique_list_numbers() -> list[int]:
    new_list = set()
    while len(new_list) <= 14:
        new_list.add(random.randint(-10, 11))

    return new_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)), len(get_unique_list_numbers()))
