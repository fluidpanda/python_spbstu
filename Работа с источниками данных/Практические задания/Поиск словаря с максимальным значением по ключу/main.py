import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME, "rt", encoding="utf-8") as file:
        data_from_json = json.load(file)

    return max(data_from_json, key=lambda x: x["score"])


if __name__ == '__main__':
    print(task())
