class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # treat each character as a node
        # build adjacency list
        # topological sort to detect cycle

        inDegree = {char: 0 for word in words for char in word}
        e = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minL = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minL] == word2[:minL]:
                return ""
            
            for j in range(minL):
                if word1[j] != word2[j]:
                    if word2[j] not in e[word1[j]]:
                        e[word1[j]].add(word2[j])
                        inDegree[word2[j]] += 1
                    break

        
        q = deque()
        res = []

        
        for c in inDegree:
            if inDegree[c] == 0: q.append(c)
        
        while q:
            cur = q.popleft()
            res.append(cur)
            for next in e[cur]:
                inDegree[next] -= 1
                if inDegree[next] == 0:
                    q.append(next)
        
        if len(res) == len(inDegree):
            return "".join(res)
        else:
            return ""