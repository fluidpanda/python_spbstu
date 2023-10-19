from icecream import ic

num = 27  # Число для проверки гипотезы Коллатца
count = 0  # Количество операций над числом

# TODO Посчитайте количество действий над числом по гипотезе Коллатца

while num != 1:
    if num % 2 == 1:
        num *= 3
        num += 1
    else:
        num /= 2
    count += 1

print("Количество действий:", count)
