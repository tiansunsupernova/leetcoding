class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            cnt = 1
            while i + cnt < len(chars) and chars[i + cnt] == chars[i]:
                cnt += 1
            chars[res] = chars[i]
            res += 1
            if cnt > 1:
                s = str(cnt)
                chars[res: res + len(s)] = list(s)
                res += len(s)
            i += cnt
        return res