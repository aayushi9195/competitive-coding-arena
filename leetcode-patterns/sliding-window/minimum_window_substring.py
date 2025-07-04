
# Time: O(N + M) (One pass over s, one pass over t)
# Space: O(M) (Because we're storing frequency maps for t and current window)
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # When t is bigger than s, we won't have an answer
        if len(t) > len(s):
            return ""

        # Keep track of left and right pointers, frequency counts of all characters in current window of s and t
        schars = {}
        left, ansLen = 0, 100001
        tchars = {}
        ans = ""

        for c in t:
            tchars[c] = tchars.get(c, 0) + 1

        # Keep a track of how many distinct characters we want and need at any point
        have, need = 0, len(tchars.keys())
        
        for right in range(len(s)):
            # Expand the current window and check if that changes the number of characters we need
            schars[s[right]] = schars.get(s[right], 0) + 1
            if s[right] in tchars and schars[s[right]] == tchars[s[right]]:
                have += 1

            # Whenever we reach a point where we find a valid window, we first update the answer
            while have == need:
                if right - left + 1 < ansLen:
                    ansLen = right - left + 1
                    ans = s[left : right+1]
                # Then we keep shrinking and updating the answer as long as it is still valid to find the minimum window
                schars[s[left]] -= 1
                if s[left] in tchars and schars[s[left]] < tchars[s[left]]:
                    have -= 1
                left += 1
                
        return ans
