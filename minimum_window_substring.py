class Solution:

    # Time: O(N)
    # Space: O(M)
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # Store counts of all characters in t
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Keep track of how many unique characters we have and need
        have, need = 0, len(countT)

        # Result string and length of the result
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            # Expand the window
            window[c] = 1 + window.get(c, 0)

            # Condition to identify if we have a character with valid frequency
            if c in countT and window[c] == countT[c]:
                have += 1

            # Now we have all that we need from t
            while have == need:
                # If we have found the new minimum
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Keep shrinking will the window is valid
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        # Return blank if no such window is found
        return s[l : r + 1] if resLen != float("infinity") else ""
