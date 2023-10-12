list_digit: int = 495184

list_of_numbers: list = []
for number in str(list_digit):
    list_of_numbers.append(int(number))

print(list_of_numbers)

print("Сумма цифр", sum(list_of_numbers))  # TODO сумма цифр
print("Количество цифр", len(list_of_numbers))  # TODO количество цифр
print("Минимальная цифра", min(list_of_numbers))  # TODO минимальная цифра
print("Максимальная цифра", max(list_of_numbers))  # TODO максимальная цифра
print("Среднее арифметическое цифр", round(sum(list_of_numbers) / len(list_of_numbers), ndigits=2))  # TODO среднее арифметическое цифр
