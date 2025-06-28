# Time: O(N)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            # At every point, the shorter bar will determine the height of the container and width will be the difference in their indices
            curr_height = min(height[left], height[right])
            curr_width = right - left
            ans = max(ans, curr_height * curr_width)
            # Move the pointer pointing to the shorter line because it's the limiting factor — moving the taller one can never increase area.
            # Reason: If we keep the shorter bar and move the other one, the area will still be determined by the shorter bar, and this time it will be lower because even though the height won't change, the width will decrease by one.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans
        
