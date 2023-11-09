# TODO написать функцию, которая выдает трехзначное число
import random


def get_random_number(length=3):
    array: list = list()
    for item in range(length):
        array.append(str(random.randint(0, 9)))

    return ''.join(array)


print(get_random_number())
