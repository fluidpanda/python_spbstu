import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, encoding="utf-8") as file_input:
        data_from_csv: list = list()
        for item in csv.DictReader(file_input):
            data_from_csv.append(item)

    with open(OUTPUT_FILENAME, "wt", encoding="utf-8") as file_output:
        json.dump(data_from_csv, file_output, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, "rt", encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
