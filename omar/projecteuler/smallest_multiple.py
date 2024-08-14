# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def is_divisible(num):
    return all(num % i == 0 for i in range(1, 21))
    # Used the all() function  to check if n is divisible by all numbers from 1 to 20.


def find_smallest_number():
    num = 2520  # Smallest number divisible by all nums 1-10 so started from here.
    while not is_divisible(num):
        num += 20
    return num

