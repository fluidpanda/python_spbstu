from icecream import ic

salary: int = 5000  # Ежемесячная зарплата
spend: int = 6000  # Траты за первый месяц
months: int = 10  # Количество месяцев, которое планируется протянуть без долгов
increase: float = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital: float = 0
month: int = 0

while months > 0:
    if months == 10:
        money_capital += salary
        money_capital -= spend
        months -= 1
        month += 1
        spend *= 1 + increase
        ic(money_capital, months, month)
    else:
        money_capital += salary
        money_capital -= spend
        spend *= 1 + increase
        months -= 1
        month += 1
        ic(money_capital, months, month)


print(f"Подушка безопасности, чтобы протянуть {month} месяцев без долгов: {abs(round(money_capital, 2))}")
