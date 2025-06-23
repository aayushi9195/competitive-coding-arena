class Solution:

    # Time: O(N) because of sliding window approach.
    # Space: O(1) because all characters are lowercase english.
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is larger than s2, its permutation cannot be found in s2.
        if len(s1) > len(s2):
            return False

        # Maintain counts of all characters in s1 and first window of same length in s2.
        s1_counts, s2_counts = [0] * 26, [0] * 26
        for i in range(len(s1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        # It means the first window itself is the permutation, so return true.
        if s1_counts == s2_counts:
            return True

        i = len(s1)
        while i < len(s2):
            # Keep sliding to the right by one character until we find a match in counts.
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i-len(s1)]) - ord('a')] -= 1
            
            if s1_counts == s2_counts:
                return True   
            i += 1
            
        return False


        
