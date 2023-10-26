# TODO Напишите функцию `is_palindrome`


def is_palindrome(string):
    string = ''.join(string.lower().split())
    new_string = string[::-1]
    return True if string == new_string else False
