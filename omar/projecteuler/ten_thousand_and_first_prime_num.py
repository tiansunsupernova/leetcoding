# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13 , we can see that the 6th prime is 13.
# What is the 10001st prime number?

def is_prime_num(num):
    if num <= 1:
        return False
    elif num == 2: # Account for 2, the only even prime number
        return True
    elif num % 2 == 0: # Not prime if even
        return False
    for i in range(3, int(num**0.5) + 1, 2): # Loop starts at 3, since 2 is covered, runs to
                                             # square root of num and increments by 2 on each iteration
        if num % i == 0: # if even return false, else true
            return False
    return True


def find_10001st_prime():
    count = 0 # count of prime numbers so sar
    number = 1
    while count < 10001: # Loop until 10001 prime numbers have been added to count
        number += 1 # increment num to check
        if is_prime_num(number):
            count += 1
    return number


# From reading, the sympy library could've reduced the above code to one line!

#from sympy import prime
# result = prime(10001)
# print(result)