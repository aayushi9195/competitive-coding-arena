class Solution:

    # Time: O(N)
    # Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            # Return as soon as we find the answer
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            # If the sum is too small, pick a bigger number
            if numbers[left] + numbers[right] < target:
                left += 1
            # If the sum is too big, pick a smaller number
            else:
                right -= 1

        # No solution found
        return []
        
