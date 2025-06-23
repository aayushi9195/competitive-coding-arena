class Solution:

    # Time: O(4**n,sqrt(n))
    # Space: O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        # Keep a track of number of open and close brackets to validate string
        def backtrack(open, close):

            # If both are equal and n/2, it means we have reached a valid combination
            if open == close == n:
                res.append("".join(stack))
                return res  
            # Open brackets should be less than half.
            if open < n:
                stack.append('(')
                backtrack(open + 1, close)
                stack.pop()
            # Close brackets can't be more than open.
            if close < open:
                stack.append(')')
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return res
        
