class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = []
        for c in s:
            if "a" <= c and c <= "z":
                li.append(c)
            elif "A" <= c and c <= "Z":
                li.append(c.lower())
            elif "0" <= c and c <= "9":
                li.append(c)
        return self.isPali("".join(li))
        
    def isPali(self, s:str) -> bool:
        i, j = 0, len(s) - 1
        while (i < j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True