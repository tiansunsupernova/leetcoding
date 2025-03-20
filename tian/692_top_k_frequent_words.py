class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        di = defaultdict(int) # k = word, v = frequency
        for w in words:
            di[w] += 1 # k = freq, v = list[words]
        h = []

        for w in di.keys():
            heapq.heappush(h, (-di[w], w))
                
        res = []

        for i in range(k):
            f, w = heapq.heappop(h)
            res.append(w)

        return res