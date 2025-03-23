class Solution:
    def addStrings(self, a: str, b: str) -> str:
        if len(a) < len(b): return self.addStrings(b, a)
        
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        res = []
        
        while i >= 0:
            if j >= 0:
                val = (int(a[i]) + int(b[j]) + c) % 10
                c = (int(a[i]) + int(b[j]) + c) // 10
            else:
                val = (int(a[i]) + c) % 10
                c = (int(a[i]) + c) // 10
            res.append(str(val))
            i -= 1
            j -= 1
        
        if c == 1:
            res.append("1")
        return "".join(reversed(res))