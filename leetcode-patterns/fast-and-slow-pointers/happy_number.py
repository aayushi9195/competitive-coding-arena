class Solution:

    # Time: O(logN)
    # Space: O(1)
    def isHappy(self, n: int) -> bool:
        
        # The sum of squares of digits eventually reaches a bounded cycle.
        # For any starting number n, the value of n quickly drops and becomes ≤ 243.
        # (Because 9² + 9² + 9² + ... is at most 243 for 9-digit numbers.)
        # So you only get at most ~243 distinct numbers before either reaching 1 or repeating a value (cycle).
        nums = set()

        # Mathematical fact: Number of digits d is at most log₁₀(n) eg. log₁₀(1234) ≈ 3.09
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            # Cycle found
            if n in nums:
                return False
            nums.add(n)
        
        return True

'''
Alternate: Floyd's cycle detection algorithm
Space: O(1)
   
def isHappy(self, n: int) -> bool:
    def get_next(n):
        return sum(int(c) ** 2 for c in str(n))

    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1
'''
