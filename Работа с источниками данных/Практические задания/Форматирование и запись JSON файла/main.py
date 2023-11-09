import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
    with open(INPUT_FILE, "rt", encoding="utf-8") as file_input:
        json_data = json.load(file_input)

    with open(OUTPUT_FILE, "wt", encoding="utf-8") as file_output:
        json.dump(json_data, file_output, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
