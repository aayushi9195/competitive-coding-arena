class Solution:
    # Time: O(N)
    # Space: O(N)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 
        # Because of the circle, we cannot rob first and last house together, we can rob only either one.
        # Break it down into two arrays, one with first to second last element and the other with second to last element.
        # Return the max profit from these two arrays as the answer.
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    # Same as house_robber.py
    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]

        
