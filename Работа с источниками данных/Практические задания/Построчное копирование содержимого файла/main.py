INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "rt", encoding="utf-8") as file_read, \
            open(OUTPUT_FILE, "wt", encoding="utf-8") as file_write:
        for line in file_read:
            file_write.write(line.upper())


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
