# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of all these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(max_limit):
    sum_of_all_nums = 0

    for multiple in range(0, max_limit):
        if multiple % 3 == 0 or multiple % 5 == 0:
            sum_of_all_nums += multiple
            print(f"Adding {multiple} to sum. Current sum is {sum_of_all_nums}.")

    return sum_of_all_nums


