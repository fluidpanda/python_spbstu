numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# numbers_initial_length = len(numbers)
# numbers_without_none = []
# index = 0
#
# for item in numbers:
#     if item is None:
#         index = numbers.index(item)
#         numbers.pop(index)
#
# numbers_sum = sum(numbers)
# numbers_average = numbers_sum / numbers_initial_length
#
# print(numbers.insert(index, numbers_average))

numbers[4] = (sum(numbers[:4]) + sum(numbers[5:])) / len(numbers)

print("Измененный список:", numbers)
