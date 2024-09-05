class Pair:
    def __init__(self, i: int, j: int, sum:int):
        self.i = i  # index for nums1
        self.j = j  # index for nums2
        self.sum = sum  # sum of nums1[i] and nums2[j]

    def __lt__(self, other):
        # This is needed for the heap to compare objects based on the sum
        return self.sum < other.sum

class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        seen = set()

        minHeap = [Pair(0, 0, nums1[0] + nums2[0])]
        seen.add((0, 0))

        while k > 0 and minHeap:
            smallest = heapq.heappop(minHeap)
            i, j = smallest.i, smallest.j
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(minHeap, Pair(i + 1, j, nums1[i+1] + nums2[j]))
                seen.add((i+1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(minHeap, Pair(i, j + 1, nums1[i] + nums2[j+1]))
                seen.add((i, j+1))
            k -= 1
        return res
