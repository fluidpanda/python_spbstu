# TODO Запишите функцию `factorial`

def factorial(n):
    counter = 1
    while n > 0:
        counter *= n
        n -= 1

    return counter


# TODO Вызовите функцию factorial и распечатайте результат
print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
