from omar.projecteuler.multiples_of_three_or_five import sum_of_multiples
from omar.projecteuler.even_fibonnacci_numbers import even_fib_numbers, generate_fib_numbers
from omar.projecteuler.smallest_multiple import find_smallest_number
from omar.projecteuler.ten_thousand_and_first_prime_num import find_10001st_prime

def main():
    # Multiple of 3 or 5 question
    # limit_for_multiple_of_3_and_5 = 1000
    # sum_of_multiples(limit_for_multiple_of_3_and_5

    # Even numbered fibonacci question
    # list_of_fib_numbers = generate_fib_numbers(4000000)
    # print(even_fib_numbers(list_of_fib_numbers))

    # Smallest multiple question
    # smallest_number = find_smallest_number()
    # print(f"The smallest positive number divisible by all numbers from 1 to 20 is: {smallest_number}")

    #10001st Prime Number question
    ten_thousand_and_first_prime_num = find_10001st_prime()
    print(ten_thousand_and_first_prime_num)


if __name__ == "__main__":
    main()
