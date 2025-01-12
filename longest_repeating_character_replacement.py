class Solution:

    # Time: O(N)where N is the length of the string.
    # Space: O(M) where M is the total number of unique characters in the string.
    def characterReplacement(self, s: str, k: int) -> int:

        # If we have the ability to replace every character then the longest substring will be the length of the string itself.
        if k >= len(s):
            return len(s)
        
        res = 0
        counts = {}
        # Track the maximum frequency seen so far.
        max_freq = 0
        l = 0

        for r in range(len(s)):
            # Slide the window
            counts[s[r]] = 1 + counts.get(s[r], 0)
            # If this character has the maximum frequency so far, update the variable.
            max_freq = max(max_freq, counts[s[r]])

            # IMP: The number of replacements is equal to the difference between the length of the substring and the frequency of the most frequent character in the string.
            # If this difference is more than k, it means the window is not valid and keep shrinking it until it is.
            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            # Update the maximum valid window size.
            res = max(res, r - l + 1)
        
        return res

        

            
        
