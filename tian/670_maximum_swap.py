class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        l = len(s)
        doswap = False
        for i in range(1, len(s)):
            if s[i] > s[i - 1]:
                doswap = True
                break
        if doswap:
            max_val, max_index = s[i], i
            for k in range(i, l):
                if s[k] >= max_val:
                    max_val = s[k]
                    max_index = k
            for j in range(i):
                if s[j] < max_val: break
            res = []
            for idx, v in enumerate(s):
                if idx == max_index: res.append(s[j])
                elif idx == j: res.append(s[max_index])
                else: res.append(v)
            s = ''.join(res)
        return int(s)