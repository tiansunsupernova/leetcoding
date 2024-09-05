class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False
        y, cur = 0, x
        while x > 0:
            digit = x % 10
            x = x // 10
            y = y * 10 + digit
        return y == cur