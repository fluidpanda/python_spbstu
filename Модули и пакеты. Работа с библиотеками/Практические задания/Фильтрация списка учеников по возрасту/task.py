# TODO Напишите функцию calculate_average_age
def calculate_average_age(students):
    ages = [student["age"] for student in students]

    return sum(ages) / len(ages)


# TODO Напишите функцию filter_students_by_age
def filter_students_by_age(students, value):
    return [student for student in students if student["age"] < value]


if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    # Вычисление среднего возраста
    # TODO Вычислите средний возраст учеников
    print("Средний возраст учеников:", calculate_average_age(students_list))

    # Фильтрация учеников по возрасту
    # TODO Офильтруйте учеников
    print("Список учеников с возрастом меньше среднего:")
    for current_student in filter_students_by_age(students_list, calculate_average_age(students_list)):
        print(current_student['name'])
