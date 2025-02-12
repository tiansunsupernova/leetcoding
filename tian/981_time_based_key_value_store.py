from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.db = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = SortedDict()
        self.db[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        
        pos = self.db[key].bisect_right(timestamp)

        if pos == 0:
            return ""
        
        return self.db[key].peekitem(pos - 1)[1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)