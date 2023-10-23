from icecream import ic

money_capital: int = 20000  # Подушка безопасности
salary: int = 5000  # Ежемесячная зарплата
spend: int = 6000  # Траты за первый месяц
increase: float = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0

while money_capital > 0:
    if month == 0:
        money_capital -= spend
        money_capital += salary
        month += 1
        spend *= 1 + increase
        ic(money_capital, spend, month)
    else:
        money_capital -= spend
        money_capital += salary
        if money_capital < 0:
            break
        month += 1
        spend *= 1 + increase
        ic(money_capital, spend, month)


print("Количество месяцев, которое можно протянуть без долгов:", month)
