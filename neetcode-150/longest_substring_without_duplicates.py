class Solution:

    # Time: O(N), where N is the length of the string
    # Space: O(M), where M is the total number of unique characters in the string
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        left, right = 0, 0
        longest = 0

        while right < len(s):
            # If the window is invalid, update it till it is valid again
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # Now the window is valid so we can add the latest character 
            window.add(s[right])
            right += 1
            
            # Update the response if we have found a larger substring
            longest = max(longest, right - left)
        
        return longest
        
