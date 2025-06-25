# Time: O(1)
# Space: O(N)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = list(nums)  # to avoid modifying the input list
        for i in range (1, len(nums)):
            self.prefix[i] += self.prefix[i-1]
        '''
        Alternative:
        from itertools import accumulate
        self.prefix = list(accumulate(self.prefix))
        '''

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - (self.prefix[left-1] if left > 0 else 0)
        
