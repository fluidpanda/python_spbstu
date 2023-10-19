from icecream import ic

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0

while money_capital > 0:
    if month == 0:
        money_capital -= spend
        money_capital += salary
        round(money_capital, 2)
        ic(money_capital, spend, month)
        month += 1
    else:
        spend *= 1.05
        money_capital -= spend
        if money_capital < 0:
            break
        money_capital += salary
        round(money_capital, 2)
        ic(money_capital, spend, month)
        month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
