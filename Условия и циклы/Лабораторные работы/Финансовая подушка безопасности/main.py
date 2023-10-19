from icecream import ic

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 1

while money_capital > 0:
    ic(money_capital, month)
    if month == 0:
        money_capital += salary
        money_capital -= spend
        month += 1
    else:
        money_capital += salary
        money_capital -= spend * 1.05
        month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
