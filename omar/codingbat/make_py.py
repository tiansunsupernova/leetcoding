# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
# make_pi() → [3, 1, 4]
import math


def make_pi():
    pi_tuple = (3, 1, 4)
    return list(pi_tuple)


def make_pi_second_solution():
    pi_str = str(math.pi)
    return [int(pi_str[0]), int(pi_str[2]), int(pi_str[3])]
