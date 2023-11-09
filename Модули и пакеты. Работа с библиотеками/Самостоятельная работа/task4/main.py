from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    coin_eagle = 0
    coin_tails = 0

    for item in range(count):
        result = choice(coin)
        if result == EAGLE:
            coin_eagle += 1
        else:
            coin_tails += 1

    list_freq.append(min(coin_eagle, coin_tails) / max(coin_eagle, coin_tails))

print(list_freq)
