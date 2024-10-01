class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp,res  = [], []
        left, right = 0, 0

        # 1. loop through, if right more than left, remove right
        # 2. run again if left more than right at end, remove left
        for i, c in enumerate(s):
            if c == '(': 
                left += 1
                temp.append(c)
            elif c == ')': 
                right += 1
                if right > left:
                    right -= 1
                else:
                    temp.append(c)
            else:
                temp.append(c)
        
        temp.reverse()

        left, right = 0, 0
        for i, c in enumerate(temp):
            if c == ')': 
                left += 1
                res.append(c)
            elif c == '(': 
                right += 1
                if right > left:
                    right -= 1
                else:
                    res.append(c)
            else:
                res.append(c)

        res.reverse()
        return res


