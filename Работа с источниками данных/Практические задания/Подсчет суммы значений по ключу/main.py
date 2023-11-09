import json


FILENAME = "input.json"


def task() -> int:
    with open(FILENAME, "rt", encoding="utf-8") as file:
        data_from_json = json.load(file)

    items = [item["contains_improvement_appeals"] for item in data_from_json]

    return sum(items)


if __name__ == '__main__':
    print(task())
