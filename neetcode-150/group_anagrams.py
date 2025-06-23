from collections import defaultdict

class Solution:

    # Time: O(MN) - N is the length of the largest string
    # Space: O(M) - M is the number of strings
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Returns a dictionary where every value is defaulted to an empty list
        groups = defaultdict(list)
        for st in strs:
            counts = self.getCountArray(st)
            # As counts is modifiable, it cannot be hashed directly
            groups[tuple(counts)].append(st)
        # To return the list of lists without the hash keys
        return groups.values()
    
    def getCountArray(self, string: str) -> List[int]:
        counts = [0] * 26
        for ch in string:
            counts[ord(ch) - ord('a')] += 1
        return counts
