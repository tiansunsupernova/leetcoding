class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        cycle = (numRows - 1) * 2
        res = []

        for row in range(numRows):
            i = row
            while i < len(s):
                res.append(s[i])
                if row != 0 and row != numRows -1:
                    gap = cycle - 2 * row
                    pos = i + gap
                    
                    if pos < len(s):
                        res.append(s[(pos)])
                i += cycle
        
        return "".join(res)