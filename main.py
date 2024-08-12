from omar.projecteuler.multiples_of_three_or_five import sum_of_multiples
from omar.projecteuler.even_fibonnacci_numbers import even_fib_numbers, generate_fib_numbers


def main():
    # Multiple of 3 or 5 question
    # limit_for_multiple_of_3_and_5 = 1000
    # sum_of_multiples(limit_for_multiple_of_3_and_5

    # Even numbered fibonacci question
    list_of_fib_numbers = generate_fib_numbers(4000000)
    print(even_fib_numbers(list_of_fib_numbers))


if __name__ == "__main__":
    main()
