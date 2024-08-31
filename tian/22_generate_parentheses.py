class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def btrack(cur, l, r):
            if (len(cur) == 2 * n):
                res.append("".join(cur))
                return
            
            if l < n:
                cur.append("(")
                btrack(cur, l + 1, r)
                cur.pop()
            if r < l:
                cur.append(")")
                btrack(cur, l, r + 1)
                cur.pop()
        
        res = []
        btrack([], 0, 0)
        return res
