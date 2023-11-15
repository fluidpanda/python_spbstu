# TODO решите задачу
import json


def task() -> float:
    with open("input.json", "rt", encoding="utf-8") as file:
        json_data = json.load(file)

    array: list = list()

    for item in json_data:
        array.append(item["score"] * item["weight"])

    generate_values = sum(array)

    return round(generate_values, 3)


print(task())
