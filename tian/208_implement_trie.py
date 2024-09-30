class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.hasWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = TrieNode()
            node = node.children[ord(c) - ord('a')]
        node.hasWord = True
        
    def search(self, word: str) -> bool:
        node = self.findPrefix(word)
        return node is not None and node.hasWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.findPrefix(prefix)
        return node is not None
    
    def findPrefix(self, prefix: str) -> TrieNode:
        node = self.root
        for c in prefix:
            if not node.children[ord(c) - ord('a')]:
                return None
            node = node.children[ord(c) - ord('a')]
        return node



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)