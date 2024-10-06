class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        left, mid, right = [],[],[]
        pivot = random.choice(points)

        for point in points:
            if self.distance(point, pivot) == 0:
                mid.append(point)
            elif self.distance(point, pivot) == -1:
                left.append(point)
            else:
                right.append(point)
        
        if k <= len(left): return self.kClosest(left, k)
        if k > len(left) + len(mid): return left + mid + self.kClosest(right, k - len(left) - len(mid))
        return left + mid[:k - len(left)]
    

    def distance(self, point1, point2) -> int:
        d1 = point1[0]** 2 + point1[1]**2
        d2 = point2[0]** 2 + point2[1]**2
        if d1 == d2:
            return 0
        elif d1 < d2:
            return -1
        else:
            return 1
        