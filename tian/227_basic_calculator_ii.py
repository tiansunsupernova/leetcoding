class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s) == 0: return 0 

        # + or - -> push only
        # * or / -> pop and calculate

        num = 0 
        st = []
        op = '+'
        for i,c in enumerate(s):
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            if not c.isdigit() and c != ' ' or i == len(s) - 1:
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                elif op == '*':
                    st.append(st.pop() * num)
                elif op == '/':
                    st.append(int(st.pop() / num))
                op = c
                num = 0
        return sum(st)
