class Solution:

    # Time: O(N)
    # Space: O(N)
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            # We found a number already seen before, so return false
            if num in s:
                return True
            # Keep adding numbers to the set as long as we have not seen them before
            s.add(num)
        return False

# Note: We can achieve the same time/space complexity by shortening the above code to a one-liner:
# return len(set(nums)) < len(nums)
