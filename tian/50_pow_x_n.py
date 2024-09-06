class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0.0
        if n == 0: return 1.0
        
        if x < 0:
            if n % 2 == 0:
                return self.myPow(-x, n)
            else:
                return  -self.myPow(-x, n)
        
        if n < 0:
            return 1.0 / self.myPow(x, - n)
        
        m = n // 2
        if n % 2 == 0:
            return self.myPow(x * x, m)
        else:
            return self.myPow(x * x, m) * x
