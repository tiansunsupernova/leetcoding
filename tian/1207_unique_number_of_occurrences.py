class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        di = defaultdict(int)
        for x in arr:
            di[x] += 1
        v = di.values()
        return len(v) == len(set(v))