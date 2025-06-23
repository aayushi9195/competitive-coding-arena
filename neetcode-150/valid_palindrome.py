class Solution:

    # Time: O(N)
    # Space: O(1)
    def isPalindrome(self, s: str) -> bool:

        # Convert input to lowercase as we need to be case-insensitive
        s = s.lower()
        i, j = 0, len(s) - 1

        while i < len(s) and j >= 0:
            # Ignore the non alphanumeric characters while being in bounds
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            # If i and j pass each other, the entire string is done 
            if i > j:
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
