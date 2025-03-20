class Solution:
    def isNumber(self, s: str) -> bool:
        # decimal + 'e' or "E" + integer
        # integer + 'e' or "E" + integer
        # decimal
        # integer
        idx = None
        for i, c in enumerate(s):
            if c == 'e' or c == "E":
                if idx: return False
                idx = i
        if not idx:
            return self.isInteger(s) or self.isDecimal(s)
        else:
            s1 = s[0:idx]
            s2 = s[idx+1:]
            return (self.isInteger(s1) or self.isDecimal(s1)) and self.isInteger(s2) 

    def isInteger(self, s):
        if len(s) == 0: return False
        for i, c in enumerate(s):
            if c == "+" or c == "-":
                if i != 0: return False
                if i == len(s) - 1: return False
            else:
                if not c.isdigit(): return False
        return True
    
    def isDecimal(self, s):
        hasDot = False
        hasDigit = False
        if len(s) == 0: return False
        for i, c in enumerate(s):
            if c == "+" or c == "-":
                if i != 0: return False
                if i == len(s) - 1: return False
            elif c == '.':
                if hasDot: return False
                if len(s) == 1: return False
                hasDot = True
            else:
                if not c.isdigit(): return False
                else: hasDigit = True
        return hasDigit

