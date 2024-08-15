class Solution:
    def simplifyPath(self, path: str) -> str:
        li = path.split("/")
        st = []
        for x in li:
            if not x or x == '.': continue
            elif x == "..":
                if st: st.pop()
            else: st.append(x)
        return "/" + "/".join(st)
        