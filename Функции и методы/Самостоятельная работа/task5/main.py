# TODO реализовать функцию
def get_sentences_list(string):
    result = [item.lstrip() for item in string.split(".") if item]

    return result


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
