class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.arr = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.arr[index]
        lo = 0
        hi = len(history) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if history[mi][0] <= snap_id and (mi == len(history) - 1 or history[mi + 1][0] > snap_id):
                return history[mi][1]
            elif history[mi][0] <= snap_id:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1 


        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)