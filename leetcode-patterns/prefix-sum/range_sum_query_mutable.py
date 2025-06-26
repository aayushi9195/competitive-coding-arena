'''
If # queries <<< # updates, we can use the naive approach - O(1) update and O(N) query
If # queries >>> # updates, we can use prefix array as a cache - O(N) update and O(1) query
If # queries === # updates and they are both large > 10^4, we need to use either segment tree or fenwick tree.

A Fenwick tree or binary indexed tree is a data structure providing efficient methods for calculation and manipulation of the prefix sums of a table of values.
Core idea: It smartly uses the mathematical concepts of power of 2 and 2's complement to determine which nodes are responsible for which index range and partial sums.
 
Space complexity for fenwick tree is O(n)
Time complexity to create fenwick tree is O(nlogn)
Time complexity to update value is O(logn)
Time complexity to get prefix sum is O(logn)

Youtube explanation: https://www.youtube.com/watch?v=CWDQJGaN1gY
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]   # Store the original values for tracking updates
        self.bit = [0] * (len(nums) + 1)   # 1-indexed BIT: bit[i] stores partial sums
        for i in range(len(nums)):
            self.insert(i+1, nums[i])   # Initialize BIT by adding each number
    
    def insert(self, ind, val):
        # Adds `val` to all relevant indices that include this index in their range.
        while ind < len(self.bit):
            self.bit[ind] += val
            ind += (ind & -ind)   # Move to next responsible node (add LSB)

    def update(self, index: int, val: int) -> None:
        # Updates the BIT to reflect this change using the difference (delta).
        diff = val - self.nums[index]
        self.nums[index] = val
        self.insert(index + 1, diff)  # Apply the difference to BIT

    def sumRange(self, left: int, right: int) -> int:
        # Returns the sum of elements from index `left` to `right` (inclusive).
        # Uses prefix sums from the BIT.
        return self.prefixSum(right+1) - self.prefixSum(left)
    
    def prefixSum(self, ind):
        # Internal method to compute prefix sum from index 1 to `index - 1` in BIT.
        sum = 0
        while ind > 0:
            sum += self.bit[ind]
            ind -= (ind & -ind)   # Move to parent node (subtract LSB)
        return sum
        
