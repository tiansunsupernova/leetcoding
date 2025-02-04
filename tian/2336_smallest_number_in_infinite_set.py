class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set() # set for all nums
        self.h = [] # minheap for all nums
        for i in range(1, 1001):
            self.nums.add(i)
            heapq.heappush(self.h, i)

    def popSmallest(self) -> int:
        x = heapq.heappop(self.h)
        self.nums.remove(x)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.add(num)
            heapq.heappush(self.h, num)



        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)