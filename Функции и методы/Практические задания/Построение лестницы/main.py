# TODO Напишите функцию print_stairs


# TODO вызвать функцию без аргументов и с аргументом равным 10


def print_stairs(n=4):
    for stair in range(1, n + 1):
        print('*' * stair)


print_stairs()
print_stairs(10)
