# TODO Напишите функцию find_common_items
from icecream import ic


def find_common_items(last_week_purchases, current_week_purchases):
    intersections = list(set(last_week_purchases).intersection(current_week_purchases))
    ic(last_week_purchases, current_week_purchases, intersections)
    return sorted(intersections)


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
