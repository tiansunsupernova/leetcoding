class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        li = []
        for c in candies:
            li.append(c + extraCandies >= maxCandy)
        return li