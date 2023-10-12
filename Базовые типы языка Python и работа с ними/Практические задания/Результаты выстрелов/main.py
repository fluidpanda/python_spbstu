results: list = [10, 8, 9, 7, 6, 9, 10, 8, 9, 10]

# TODO Вычислите необходимые значения
average: int = sum(results) / len(results)
min_score: int = min(results)
max_score: int = max(results)

print("Среднее арифметическое результатов выстрелов:", average)
print("Наименьшее количество очков за выстрел:", min_score)
print("Наибольшее количество очков за выстрел:", max_score)
