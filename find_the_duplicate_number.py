class Solution:
    # Time: O(N)
    # Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        # Because the numbers are between 1 and N and the size of the list is N+1, we can use the idea of using number-1 as the index i.e. position in the array. As every other integer appears only once, their positions in the list will be fixed. For the number that appears more than once, we can identify that by checking if its position is already full or not.
        for num in nums:
            # We iterate through the array using index i. For each element, we use its absolute value to find the corresponding index and mark that position as negative. Taking absolute value ensures we work with the original value even if it’s already negated.
            index = abs(num) - 1
            # If we encounter a number whose corresponding position is already negative, it means the number is a duplicate, and we return it.
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
        return -1
        
