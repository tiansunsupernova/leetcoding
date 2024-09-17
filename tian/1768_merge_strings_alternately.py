class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = max(len(word1), len(word2))
        li = []
        for i in range(l):
            if i < len(word1):
                li.append(word1[i])
            if i < len(word2):
                li.append(word2[i])
        return "".join(li)