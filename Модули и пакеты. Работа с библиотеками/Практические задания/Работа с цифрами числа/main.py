number = 2342354235235

list_digits = ...  # TODO c помощью list comprehension получить список цифр числа

print(sum([int(item) for item in str(number)]))  # TODO найти сумму цифр числа
print(sum([int(item) for item in str(number) if int(item) % 2 == 0]))  # TODO найти сумму всех четных чисел
print(len(str(number)))  # TODO найти количество цифр
print(min([int(item) for item in str(number)]))  # TODO найти минимальную цифру
print([int(item) for item in str(number)][0] - [int(item) for item in str(number)][-1])  # TODO найти разность между первой и последней цифрой
