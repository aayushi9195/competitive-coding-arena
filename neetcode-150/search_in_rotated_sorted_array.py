class Solution:

    # Time: O(logN)
    # Space: O(1)
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # Find which half is sorted
            # Ensures that even when nums[left] == nums[mid], the left half is correctly identified as sorted.
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            #  Avoids incorrectly treating the right half as sorted when nums[mid] == nums[right].
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

'''
Why <=?
If nums[left] == nums[mid], the left half is still sorted. For example:
Array: [2, 2, 3, 4, 1]
left = 0 (nums[left] = 2), mid = 1 (nums[mid] = 2)
Even though nums[left] == nums[mid], the left half [2, 2, 3, 4] is sorted.
Using <= ensures that edge cases where all elements in the left half are the same are still correctly handled.

Why <?
When nums[mid] == nums[right], the algorithm cannot guarantee which side (left or right) contains the rotation point.
In cases like [5, 6, 1, 2, 2], even though the right subarray [2, 2] is technically sorted, it might still include the rotation point.
'''
        
