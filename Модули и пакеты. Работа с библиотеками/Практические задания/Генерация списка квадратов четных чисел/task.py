def generate_even_squares(n):
    """
    Функция для генерации списка квадратов четных чисел от 0 до N.
    """
    # TODO Замените на list comprehension c условием фильтрации
    return [item**2 for item in range(n + 1) if item % 2 == 0]


if __name__ == '__main__':
    # Проверка работы функции
    print(generate_even_squares(5))  # [0, 4, 16]
    print(generate_even_squares(10))  # [0, 4, 16, 36, 64, 100]
    print(generate_even_squares(0))  # [0]
