numbers: list = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# numbers_without_none: list = []
# none_indexes: list = []
# numbers_result: list = []
# numbers_len = len(numbers)
#
# получаем список с числами без None и получаем список индексов None
# for item in numbers:
#     if item is not None:
#         numbers_without_none.append(item)
#     if item is None:
#         none_indexes.append(numbers.index(item))
#
# numbers_sum = sum(numbers_without_none)
#
# for item in numbers_without_none:
#     numbers_result.append(item)
#     for number in none_indexes:
#         if numbers_without_none.index(item) == number - 1:
#             numbers_result.append(numbers_sum / numbers_len)
# какое-то кривое решение получилось

numbers[4] = (sum(numbers[:4]) + sum(numbers[5:])) / len(numbers)

# print("Измененный список:", numbers_result)
print("Измененный список:", numbers)
