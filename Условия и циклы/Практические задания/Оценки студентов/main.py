# Список словарей со студентами и их оценками
from icecream import ic


students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]

# TODO Распечатать имена студентов с оценками выше тройки

for student in students:
    if student["grade"] > 3:
        print(f"{student['name']}. Оценка: {student['grade']}")
