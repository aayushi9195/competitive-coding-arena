class Solution:
    # Time: O(N^2)
    # Space: O(N^2)
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        # If the substring from i to j is a palindrome, dp[i][j] will be True. Set all indices to False initially.
        dp = [[False] * n for _ in range(n)]
        start, length = 0, 1

        # All strings with length 1 are palindromes.
        for i in range(n):
            dp[i][i] = True

        # Check if strings with length 2 are palindromes or not and update the start index and max length accordingly.
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start, length = i, 2

        # For every substring of length 3 to n
        for k in range(3, n+1):
            # Consider all possible substrings of length k
            for i in range(n-k+1):
                j = i+k-1
                # Current substring i to j is a palindrome if they outermost characters are same and the inner substring i.e. i+1 to j-1 is also a palindrome.
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    # Update the start index and max length if we find a larger palindrome.
                    start, length = i, k
                  
        # Return the substring which is the longest palindrome in the input string.
        return s[start : start + length]

'''
Note:
1. Space can be reduce to O(1) in the above solution if we pick every i from 0 to N and keep expanding around it in both directions while comparing characters to see if it is a palindrome or not.
2. Check Manacher's algorithm for O(N) time and O(N) space. It is a bit complicated to understand and implement.
'''
