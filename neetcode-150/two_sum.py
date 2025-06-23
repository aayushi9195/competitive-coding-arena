class Solution:

    # Time: O(N)
    # Space: O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number -> index
        s = {} 
        for i, n in enumerate(nums):
            if target - n in s:
                # smaller index needs to be returned first
                return [s[target - n], i]
            # store the current number and its index until we find the result
            s[n] = i
        # could not find any pair whose sum is target
        return [-1, -1]
