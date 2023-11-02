# TODO реализовать функцию
def remove_whitespace(string):
    result = [item for item in string.split(" ") if item]

    return " ".join(result)


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
