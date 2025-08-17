class Solution:
    # Time: O(LogN)
    # Space: O(1)
    def findMin(self, nums: List[int]) -> int:

        # Edge case
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        # Binary search
        while left <= right:
            mid = left + (right - left) // 2

            # If the previous element is smaller, it means we have found the minimum element!
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]

            # If the whole subarray is sorted, we know left is the minimum element
            if nums[left] < nums[right]:
                return nums[left]

            # If left half is sorted, the array is rotated and minimum lies in the other half
            if nums[left] <= nums[mid]:
                left = mid + 1
            # If right half is sorted, the array is rotated and minimum lies in the other half
            else:
                right = mid - 1

        # We will not reach here
        return -1
