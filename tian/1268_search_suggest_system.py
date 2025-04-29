class Node:
    def __init__(self):
        self.child = {}
        self.cnt = 0
        self.li = []

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addword(self, word):
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
            node.cnt += 1
            if node.cnt <= 3: node.li.append(word)

    def searchword(self, word):
        res = []
        node = self.root
        no_result = False
        for i in range(len(word)):
            c = word[i]
            if no_result:
                res.append([])
                continue
            if c in node.child:
                node = node.child[c]
                res.append(node.li)
            else:
                res.append([])
                no_result = True
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for w in products:
            trie.addword(w)
        return trie.searchword(searchWord)