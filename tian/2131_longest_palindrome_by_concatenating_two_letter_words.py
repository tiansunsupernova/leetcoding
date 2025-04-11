class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        di = defaultdict(int)
        res = 0
        for w in words:
            di[w] += 1
        
        hasmid = False
        keys = list(di.keys())
        
        for w in keys:
            if w[0] == w[1]:
                if di[w] % 2 == 1:
                    res += di[w] - 1
                    hasmid = True
                else:
                    res += di[w]
            elif w[0] < w[1]:
                res += 2 * min(di[w], di[w[1] + w[0]])

        if hasmid: res += 1
        return res * 2
                
        