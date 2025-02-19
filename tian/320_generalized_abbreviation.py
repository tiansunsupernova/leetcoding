class Solution:
    
    def __init__(self):
        self.res = []

    def generateAbbreviations(self, word: str) -> List[str]:
        self.btrack(word, 0, False, "")
        return self.res

    @lru_cache
    def btrack(self, word, i, last_number, cur):
        if i == len(word):
            self.res.append(cur)
        # 1. use word[i] as char
        if i < len(word):
            cur += word[i]
            self.btrack(word, i+1, False, cur)
            cur = cur[:-1]

        # 2. use word[i] as part of a number
        if not last_number:
            for j in range(i + 1, len(word) + 1):
                num = str(j - i)
                cur += num
                self.btrack(word, j, True, cur)
                cur = cur[:-len(num)]


            
        
