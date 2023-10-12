# TODO исправьте опечатку в слове

fruits: list = ["яблоко", "банан", "опельсин", "виноград"]
correction = "а" + fruits[2][1:]
fruits[2] = correction

print(fruits)
