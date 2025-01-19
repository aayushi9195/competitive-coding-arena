class Solution:

    # Time: O(logN)
    # Space: O(1)
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = int(l + (r - l) / 2)
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1

# Note: There is an inbuilt function bisect.bisect_left that can also be used and it works with the same time complexity. 
        
        
