class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0 for _ in range(len(code))]
        if k == 0: return res
        if k < 0:
            s = sum(code[k:])
        else:
            s = sum(code[0:1+k])
        for i, x in enumerate(code):
            if k > 0:
                s -= code[i]
                res[i] = s
                s += code[(1 + k + i) % len(code)]
            else:
                res[i] = s
                s = s + code[i] - code[(i + k) % len(code)]
        return res