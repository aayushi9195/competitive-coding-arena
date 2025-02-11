class TrieNode:
    def __init__(self):
        # We are using a fixed-sized array here as the input string will always have lowercase english characters.
        # If there are no such restrictions, we should use a dictionary here to support all kinds of characters.
        self.node = [None] * 26
        self.is_end = False

# Time: O(N) for each function call where N is the length of the string.
# Space: O(T) where T is the total number of nodes created in the trie.
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            # If it is a dictionary instead, use "if ch not in temp.node: temp.node[ch] = TrieNode()". We also would not need to calculate index.
            if not temp.node[index]:
                temp.node[index] = TrieNode()
            temp = temp.node[index]
        # Keep adding characters in the trie as per its design and mark the end of the word as true.
        temp.is_end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not temp.node[index]:
                return False
            temp = temp.node[index]
        # If we don't find a character or if we see that the word is not ending where we expect it to, return false.
        return temp.is_end

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not temp.node[index]:
                return False
            temp = temp.node[index]
        # Almost same as search but here we don't need to check end of word as we are only looking for the prefix i.e. it may or may not be a complete word.
        return True
        
        
