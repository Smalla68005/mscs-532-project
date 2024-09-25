class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes; keys are characters, values are TrieNodes
        self.children = {}
        self.is_end_of_pattern = False

class Trie:
    def __init__(self):
        # The root node of the trie, initialized as a TrieNode
        self.root = TrieNode()

    # Method to insert a pattern (string) into the trie
    def insert(self, pattern):
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("Invalid patten. Pattern must be a non-empty string")
        
        node = self.root  # Start from the root node
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_pattern = True

    # Method to search for a pattern in the trie
    def search(self, pattern):
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("Invalid pattern. Pattern must be a non-empty string.")
        
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_pattern
