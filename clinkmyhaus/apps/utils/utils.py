import random


def random_pic(a: int, b: int):
    random_num = str(random.randint(a, b))
    if len(random_num) < 2:
        return '0%s' % random_num
    return random_num
