class Solution:

    # Time: O(N)
    # Space: O(N)
    def isValid(self, s: str) -> bool:

        mappings = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch not in mappings:
                stack.append(ch)
            else:
                # If no. of closing brackets are > opening or if this closing does not have a matching opening then return false.
                if not stack or stack.pop() != mappings[ch]:
                    return False

        # Stack can be non-empty if no. of opening brackets > closing. In that case also the string is invalid. 
        return True if not stack else False
        
