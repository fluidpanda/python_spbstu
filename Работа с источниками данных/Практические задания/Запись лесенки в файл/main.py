INPUT_FILE = "input.txt"


OUTPUT_FILE = "output.txt"


def task(n=10):
    with open(OUTPUT_FILE, "wt", encoding="utf-8") as file:
        for stair in range(1, n + 1):
            file.write(f'{"*" * stair}\n')


if __name__ == '__main__':
    # Необходимо для проверки
    task()
    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
