def generate_squares(n):
    """
    Функция для генерации списка квадратов целых чисел от 0 до N.
    """
    # TODO заменить на list comprehension
    return [item**2 for item in range(n + 1)]


if __name__ == '__main__':
    # Проверка работы функции
    print(generate_squares(5))  # [0, 1, 4, 9, 16, 25]
    print(generate_squares(10))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(generate_squares(0))  # [0]
