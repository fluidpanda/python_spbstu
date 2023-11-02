def is_lucky_number(num: int) -> bool:
    ...  # TODO проверить что число шестизначное и положительное
    if len(str(num)) != 6 and num < 0:
        raise ValueError(f"Число {num} меньше нуля и не шестизначное")
    # TODO проверить счастливое число или нет
    array = [int(item) for item in str(num)]
    return sum([item for item in array[:3]]) == sum([item for item in array[3:]])


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
