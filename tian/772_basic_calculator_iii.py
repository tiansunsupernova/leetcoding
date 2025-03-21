class Solution:
    def eval(self, operator, x, y = 0):
            if operator == "+":
                return x
            if operator == "-":
                return -x
            if operator == "*":
                return x * y
            return int(x / y)

    def calculate(self, s: str) -> int:
        num = 0
        st = []
        last_sign = "+"
        s += "@"

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                st.append(last_sign)
                last_sign = "+"
            else:
                if last_sign in "*/":
                    st.append(self.eval(last_sign, st.pop(), num))
                else:
                    st.append(self.eval(last_sign, num))
                num = 0
                last_sign = c
                if c == ")":
                    while type(st[-1]) == int:
                        num += st.pop()
                    last_sign = st.pop()
        print(st)
        return sum(st)
            