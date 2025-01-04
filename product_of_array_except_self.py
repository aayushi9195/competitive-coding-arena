class Solution:
    # Time: O(N)
    # Space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # stores the left product so far
        prefix = 1
        for i in range(len(nums)):
            # result should not contain the current element, so set result as the product so far
            res[i] = prefix
            # and then add the current element to the prefix which becomes the product so far for the next number
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # we already have the left product, now apply the same logic from right to left but this time we need to multiply with already existing product in the result
            res[i] *= postfix
            # add current number after setting the result so current number is excluded from current product and included in the next product
            postfix *= nums[i]
        return res

# Note: O(N) space solution involves keeping two arrays to store the product so far from both left and right directions. Then the result can use left and right products to get the final product.
