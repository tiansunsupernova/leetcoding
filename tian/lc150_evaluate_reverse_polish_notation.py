class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for x in tokens:
            if x == "+":
                st.append(st.pop() + st.pop())
            elif x == "-":
                st.append(st.pop() - st.pop())
            elif x == "*":
                st.append(st.pop() * st.pop())
            elif x == "/":
                v1 = st.pop()
                v2 = st.pop()
                st.append(int(v2 / v1))
            else:
                st.append(int(x))
        return st.pop()

