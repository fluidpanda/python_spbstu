import json


FILENAME = "input.json"


def task() -> list[dict]:
    with open(FILENAME, encoding="utf-8") as f:
        json_data = json.load(f)

    def func(x):
        return x["id"]

    return sorted(json_data, key=func)


if __name__ == '__main__':
    # Необходимо для проверки
    data = task()
    print(json.dumps(data, indent=4))
