class Solution:
    # Time: O(logN)
    # Space: O(1)
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1
        # The goal is to shrink the search range (left to right) and eventually isolate the minimum element. Whether mid is included or excluded depends on which side of the array mid is located in.
        while left < right:
            mid = left + (right - left) // 2

            # This means the middle element is smaller than the rightmost element. This tells us that the minimum element is either at mid or to the left of mid because the right portion (from mid to right) is sorted.
            if nums[mid] < nums[right]:
                # This keeps mid in the search range because mid might be the minimum.
                right = mid
            # This means the middle element is greater than or equal to the rightmost element. This tells us that the minimum element is to the right of mid because the rotation point must be in that portion.
            else:
                # This excludes mid from the search range because we know the minimum cannot be at mid.
                left = mid + 1
        
        return nums[left]
