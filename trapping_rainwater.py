class Solution:
    '''
    Logic: For end blocks i.e. first and last element of array we cannot trap any water. For the rest, the minimum of the max left height and max right height will determine the water height. That will need to be reduced by height of the current block.
    Explanation: https://leetcode.com/problems/trapping-rain-water/solutions/1374608/c-java-python-maxleft-maxright-so-far-with-picture-o-1-space-clean-concise/?orderBy=most_votes
    '''
    # Time: O(N)
    # Space: O(1)
    def trap(self, height: List[int]) -> int:

        n = len(height)

        if n <= 2:
            return 0

        total_water = 0

        # optimising to constant space
        max_left, max_right = height[0], height[n-1]

        # as we go along the way from both ends, we update the max if needed and keep trapping water at every left/right
        left, right = 1, n-2

        while left <= right:
            
            # it means at this point, left height is going to determine the trapped water
            if max_left < max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            
            # it means at this point, right height is going to determine the trapped water
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1
        
        return total_water
