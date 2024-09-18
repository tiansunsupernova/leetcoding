class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt, l = 0, len(flowerbed)
        for i in range(l):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == l - 1 or flowerbed[i + 1] == 0):
                cnt += 1
                flowerbed[i] = 1
        return n <= cnt