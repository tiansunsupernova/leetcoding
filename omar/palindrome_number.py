class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        turn_x_to_string = str(x)

        # check if string is = to its reverse
        # [::1] would compare string to what it is currently. [::-1] is its reverse
        return turn_x_to_string == turn_x_to_string[::-1]
