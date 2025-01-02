class Solution:

    # Time: O(M+N)
    # Space: O(1)
    def isAnagram(self, s: str, t: str) -> bool:

        # If both strings are null then they are anagrams
        if not s and not t:
            return True

        # If only one string is null, then return false
        if not s or not t:
            return False

        # If the strings are not of same length then no point comparing them
        if len(s) != len(t):
            return False

        # As we know strings can only have lowercase letters we can use constant space
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        # If the strings are anagrams, no letter will have a non-zero frequency
        for c in counts:
            if c != 0:
                return False
        return True
        
