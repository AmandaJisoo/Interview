class TrieNode:
    def __init__(self):
        self.childern = {}
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.childern:
                node.childern[char] = TrieNode
            node = node.childern[char]
        node.isEnd = False
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.childern:
                return False
            node = node.childern[char]
        return node.isEnd
    
    def startsWith(Self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.childern:
                retuen False
            node = node.childern[char]
        return node.isEnd
    
    def delete(self, word):
        def recursive(node, word, i):
            #last char index
            if i == len(word):
                if not node.isEnd:
                    return False
                node.isEnd = False
                return len(node.childern) == 0
            #word is not in the trie
            if word[i] not in node.childern:
                return False
            needToDelete = recursive(node.childern[word[i]], word, i + 1)
            if needToDelete:
                node.childern.pop(word[i])
                return len(node.childern) == 0
            return False
        
            