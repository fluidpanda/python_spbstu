list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
counter_odd: int = 0
counter_even: int = 0
# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных
for number in list_:
    if number % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1
# TODO вывести каких чисел больше
if counter_even > counter_odd:
    print("Четных чисел больше")
elif counter_odd > counter_even:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")