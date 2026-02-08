import math


def find_next_square(sq):
    a = math.sqrt(sq)
    if a == int(a):
        return int((a+1) * (a+1))
    return -1


print(find_next_square(121))
