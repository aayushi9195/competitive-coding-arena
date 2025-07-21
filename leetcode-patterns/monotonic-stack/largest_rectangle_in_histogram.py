class Solution:
    # Time: O(N)
    # Space: O(N)
    def largestRectangleArea(self, heights: List[int]) -> int:
      
        stack = []
        ans = 0

        # For every bar, if we find taller bars in the stack, it means those taller bars cannot be extended to the right.
        # So we find the largest area with the taller bars and update the answer.
        # We also update the left boundary of current bar because its height is smaller, so area can be extended further left.
        for i, curr in enumerate(heights):
            start = i
            while stack and stack[-1][1] > curr:
                j, h = stack.pop()
                ans = max(ans, h * (i-j))
                start = j
            # Push the leftmost possible boundary with the current bar and its height on the stack.
            stack.append((start, curr))

        # This happens when some or all bars don't have a smaller bar to the right. Eg [1,2,3,4]
        # In this case each bar's rectangle (right boundary) can be extended till the end of the list.
        while stack:
            j, h = stack.pop()
            ans = max(ans, (len(heights) - j) * h)

        return ans
