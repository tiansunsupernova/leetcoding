class Solution:
    def decodeString(self, s: str) -> str:
        st, res = [], []
        cnt = 0
        cur = ""
        for i in range(len(s)):
            if s[i].isdigit(): 
                cnt = cnt * 10 + int(s[i])
            elif s[i] == '[':
                st.append((cur, cnt))
                cnt = 0
                cur = ""
            elif s[i] == ']':
                cur1, cnt1 = st.pop()
                cur = cur1 + cnt1 * cur
            else:
                cur += s[i]

        return cur
