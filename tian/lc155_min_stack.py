class MinStack:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, val: int) -> None:
        self.st1.append(val)
        if not self.st2 or self.st2[-1] >= val:
            self.st2.append(val)


    def pop(self) -> None:
        val = self.st1.pop()
        if val == self.st2[-1]:
            self.st2.pop()
        

    def top(self) -> int:
        return self.st1[-1]
        

    def getMin(self) -> int:
        return self.st2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()