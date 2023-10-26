def get_list_number_divisors(number):
    # TODO Найдите список делителей числа number
    array: list = []
    for it in range(1, number + 1):
        if number % it == 0:
            array.append(it)

    return array


print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
