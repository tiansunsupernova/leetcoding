class Node:
    def __init__(self):
        self.cnt = 0
        self.next = {}

class Solution:

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # score(x) how many words have prefix words x
        # answer[y] sum(score[k]) where k is all prefixes of y
        # ["abc","ab","bc","b"]
        # ans = []
        root = Node()
        for w in words:
            self.add(root, w)  
        res = []
        for w in words:
            res.append(self.get(root, w)) 
        return res

    # add string st to trie
    def add(self, node, st):
        for c in st:
            if c not in node.next:
                node.next[c] = Node()
            node = node.next[c]
            node.cnt += 1

    # get the answer of st
    @lru_cache(None)
    def get(self, node, st):
        res = 0
        for c in st:
            node = node.next[c]
            res += node.cnt
        return res
