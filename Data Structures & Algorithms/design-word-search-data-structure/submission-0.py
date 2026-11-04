class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.eow = True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, i):
            if i == len(word):
                return node.eow
            
            ch = word[i]

            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                
            if ch not in node.children:
                return False
            
            return dfs(node.children[ch], i + 1)

        return dfs(node, 0)
        
