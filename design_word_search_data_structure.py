class TrieNode:
   # Choose dictionary over array here as we would need to do DFS for wildcard character.
    def __init__(self):
        self.children = {} # character -> TrieNode
        self.word = False

# Time: O(N) for add word and search
# Space: O(T + N) where N is the length of the string and T is the total number of nodes created in trie
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        # Helper method to let us explore every option for . character and backtrack
        def dfs(j, root):
            cur = root
            # We need this to understand how much of the string is remaining i.e. start to j is already found so we need to resume with j and go till the end of the word.
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # For ., we can match that with any character, so if any of the child trees returns True, we can return True.
                    # We use i+1 as we need to continue looking for the next character.
                    # curr.children has all possible characters at this point, we are not interested in the keys because . can match with anything. For the next iteration we need the values i.e. the characters that are reachable from any key at this level of the trie.
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # If curr character is not . and not found, return False.
                    if c not in cur.children:
                        return False
                    # Else traverse down the trie.
                    cur = cur.children[c]
            # Check that this is the end of word.
            return cur.word
          
        # We need to find the entire string starting from root.
        return dfs(0, self.root)
