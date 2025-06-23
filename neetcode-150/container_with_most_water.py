class Solution:

    # Time: O(N)
    # Space: O(1)
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:

            # Water contained = area = length * height
            # Length = distance between two indices
            # Height = minimum of left and right heights
            curr_height = min(heights[left], heights[right])
            curr_width = right - left

            # Update the response if we observe a larger area
            max_water = max(max_water, curr_height * curr_width)

            # IMP: We move the pointer whose height is minimum. Because the area is determined by the minimum of the two heights.
            # Eg: In [1,7,2,5,4,7,3,6], if left and right are 0 and 7 respectively, curr_height = min(1, 6) = 1. If we decrement right, the next height maybe either > or < 1. If it is > 1, then the curr_height will still be 1 but we will have a lower area because the width has now reduced as we contracted the array. If it is < 1, the total area will still be lower than the last one, because both curr_height and curr_width will be lesser than before. That's why we should increment left and keep right as is.
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
