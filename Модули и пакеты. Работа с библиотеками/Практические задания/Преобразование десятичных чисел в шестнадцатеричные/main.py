# TODO Напишите функцию decimal_to_hex
def decimal_to_hex():
    return {number: hex(number) for number in range(16)}


if __name__ == '__main__':
    print(decimal_to_hex())  # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами
