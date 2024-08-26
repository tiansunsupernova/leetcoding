# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
# A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:  # one or any number less than one cannot be a perfect number so false right away
            return False

        divisors_sum = 1  # Start with 1 since 1 is a divisor of every positive integer
        sqrt_num = int(num ** 0.5)

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i

        return divisors_sum == num

# Time Complexity of O(sqrt(n)) because the algorithm iterates up to the square root of the input number.
# Space Complexity O(1) is O(1) as it uses a constant amount of extra space regardless of the input size.
