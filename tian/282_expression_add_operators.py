class Solution:
    def __init__(self):
        self.ans = []

    def addOperators(self, num: str, target: int) -> List[str]:
        self.btrack(num, target, 0, "", 0, 0)
        return self.ans

    def btrack(self, num, target, i, exp, res, last):
        if i == len(num):
            if res == target: self.ans.append(exp)
            return
        cur = int(num[i])

        for j in range(i, len(num)):
            n = int(num[i: j+1])
            if i == 0:
                self.btrack(num, target, j + 1, str(n), n, n)
            else:
                # +
                self.btrack(num, target, j + 1, exp + "+" + str(n), res + n, n)
                # -
                self.btrack(num, target, j + 1, exp + "-" + str(n), res - n, -n)
                # *
                self.btrack(num, target, j + 1, exp + "*" + str(n), res - last + last * n , last * n)
            if n == 0:
                break
            
