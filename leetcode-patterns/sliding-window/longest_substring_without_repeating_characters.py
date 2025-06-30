class Solution:
    # Time: O(N)
    # Space: O(min(N, M)) = N unique characters in the worst case (if all characters are different). But more realistically, M, the size of the character set (e.g., 26 for lowercase letters, 128 for ASCII).
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        chars = set()
        while right < len(s):
            # Keep expanding the window until we see unique characters
            while right < len(s) and s[right] not in chars:
                chars.add(s[right])
                right += 1
            # Either we have reached the end of the string or found a duplicate, so update the max answer
            ans = max(ans, right - left)
            # Keep shrinking the window until we get rid of duplicates to get a valid window again
            while right < len(s) and s[right] in chars:
                chars.remove(s[left])
                left += 1
        return ans
      
        '''
        Shorter code:

        left = 0
        chars = set()
        ans = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            ans = max(ans, right - left + 1)
        return ans

        Steps to remember:
        For every character in the string,
        1. Remove the duplicates first to make the current window valid
        2. Expand the window by adding this character
        3. Update the answer
        '''
