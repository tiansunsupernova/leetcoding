class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        st = []
        res = 0

        for c in s:
            if c == ' ': continue
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                st.append(res)
                st.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * num
                res *= st.pop()
                res += st.pop()
                num = 0
            elif c in "+-":
                res += num*sign
                num = 0
                sign = 1 if c == "+" else -1
        
        return res + sign * num  


