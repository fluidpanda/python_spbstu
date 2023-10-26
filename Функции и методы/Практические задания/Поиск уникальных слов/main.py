# TODO реализовать функцию
def get_unique_words(string):
    string = list(set(string.split()))
    string.sort()

    return string


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
