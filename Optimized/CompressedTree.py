class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_pattern = False

class CompressedTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_pattern = True

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_pattern

    def compress_trie(self):
        """ Compress the trie by merging common prefixes. """
        def compress(node):
            if len(node.children) == 1 and not node.is_end_of_pattern:
                char, child = list(node.children.items())[0]
                node.is_end_of_pattern = child.is_end_of_pattern
                node.children = child.children
                return char + compress(child)
            return ""

        compress(self.root)
