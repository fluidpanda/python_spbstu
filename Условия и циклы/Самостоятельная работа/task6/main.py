list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию

index_max: int = 0
value_max: int = list_numbers[index_max]

for index, value in enumerate(list_numbers):
    if value >= value_max:
        value_max = value
        index_max = index

list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
