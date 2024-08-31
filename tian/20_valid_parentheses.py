class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                st.append(c)
            elif c == ")":
                if not st or st.pop() != "(": return False
            elif c == "]":
                if not st or st.pop() != "[": return False
            elif c == "}":
                if not st or st.pop() != "{": return False
        return len(st) == 0