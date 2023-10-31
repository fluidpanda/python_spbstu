from time import time


def count_letters(text):
    text = text.lower()
    frequency = {}
    for letter in text:
        if letter.isalpha():
            # frequency[letter] = text.count(letter)
            if frequency.get(letter):
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    return frequency


def calculate_frequency(dictionary):
    letters_count = sum(dictionary.values())
    frequency = {}
    for value in dictionary:
        frequency[value] = f"{dictionary[value] / letters_count:.2f}"
    # return frequency
    result = list()
    for key, item in frequency.items():
        result.append(f'{key}: {item}\n')
    result[-1] = result[-1][:-1]
    return ''.join(result)


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

t1 = time()
print(calculate_frequency(count_letters(main_str)))
print(time() - t1)  # 0.000997781753540039
# dict_ = calculate_frequency(count_letters(main_str))
# for key, value in dict_.items():
#     print(f"{key}: {value}")
