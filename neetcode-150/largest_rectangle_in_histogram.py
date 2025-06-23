class Solution:

    # Time: O(N)
    # Space: O(N)
    def largestRectangleArea(self, heights: List[int]) -> int:

        # For a bar with height h, try extending it to the left and right. We can see that we can't extend further when we encounter a bar with a smaller height than h. The width will be the number of bars within this extended range. A brute force solution would be to go through every bar and find the area of the rectangle it can form by extending towards the left and right.
        # The left and right boundaries are the positions up to which we can extend the bar at index i. The area of the rectangle will be height[i] * (right - left + 1), which is the general formula for height * width. These boundaries are determined by the first smaller bars encountered to the left and right of the current bar.
        stack = []
        max_area = 0

        # We are maintaining a monotonically increasing stack.
        # If the current bar is higher than the top of the stack, push it to the stack. Because the bars already in the stack can still be extended.
        # If the current bar is lower than the top of the stack, all the bars seen so far cannot be extended beyond this point. Area formed by them will be their own height and difference between their positions and current position. Now push the current bar on the stack, but use the position of the last popped element for this bar. WHY? Because the height of this bar is lower, it can be extended to the left as the bars in the stack were taller.
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # This is the TRICKIEST step.
                start = index
            stack.append((start, h))

        # In the end if the elements are still on the stack, it means there was no lower bar to their right i.e. they can be extended till end of the list.
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
        
