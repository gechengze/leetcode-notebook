# leetcode submit region begin(Prohibit modification and deletion)
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isend = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            c = ord(c) - ord('a')
            if not node.children[c]:
                node.children[c] = Trie()
            node = node.children[c]
        node.isend = True

    def search_prefix(self, prefix):
        node = self
        for c in prefix:
            c = ord(c) - ord('a')
            if not node.children[c]:
                return None
            node = node.children[c]

        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.isend

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
