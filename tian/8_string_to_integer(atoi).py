class Solution:
    def myAtoi(self, s: str) -> int:
        # leading space
        s = s.lstrip()
        # signed
        if len(s) == 0: return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif  s[0] == '+':
            sign = 1
            s = s[1:]
        else: sign = 1
        # conversion
        num = []
        for c in s:
            if c.isdigit():
                num.append(c)
                if num[0] == '0':
                    num = []
            else: break
        
        if len(num) == 0: return 0
        res = sign * float("".join(num))
        res = min(res, 2 ** 31 - 1)
        res = max(res, - 2 ** 31)
        return int(res)
        

