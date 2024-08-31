import random

class RandomizedSet:

    def __init__(self):
        self.dict = {} #{values, index}
        self.li = [] #[values]

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.li)
        self.li.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            pos = self.dict[val]
            lastval = self.li[-1]
            self.li[pos]= lastval
            self.dict[lastval] = pos
            self.li.pop()
            del self.dict[val]
            return True
        return False


    def getRandom(self) -> int:
        return random.choice(self.li)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()