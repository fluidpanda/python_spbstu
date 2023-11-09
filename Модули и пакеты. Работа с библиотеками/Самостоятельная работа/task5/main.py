import random
import string


def get_random_password(length=8) -> str:
    data_set = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.sample(data_set, length))


print(get_random_password())
