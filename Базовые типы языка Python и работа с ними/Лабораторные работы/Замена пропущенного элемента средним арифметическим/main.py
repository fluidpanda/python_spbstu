numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


numbers_without_none: list = []

for item in numbers:
    if item is not None:

numbers[4] = (sum(numbers[:4]) + sum(numbers[5:])) / len(numbers)

print("Измененный список:", numbers)
