# Time: O(N)
# Space: O(1)
class Solution:

    # Don't use the bisect module here as it will take O(NlogN) time (for every number, find where it's complement i.e. target-number is).
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]   # 1-indexed
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]   # Should never reach here if one solution exists
        
