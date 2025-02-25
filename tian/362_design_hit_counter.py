class HitCounter:

    def __init__(self):
        self.q = deque()
        

    def hit(self, timestamp: int) -> None:
        self.remove(timestamp)
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        self.remove(timestamp)
        return len(self.q)

    def remove(self, timestamp) -> None:
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)