'''
Let's say:
nums = [1, 3, 4, 2, 2]
#       0  1  2  3  4
So n = 4, values are from 1 to 4, but there are 5 elements → there must be a duplicate.

Step 1: Think of nums as a function: f(i) = nums[i]
So from index i, we jump to nums[i]. It’s like a “pointer” from node i to nums[i].

Let's follow the jumps:
Start at index 0:
nums[0] = 1 → go to index 1  
nums[1] = 3 → go to index 3  
nums[3] = 2 → go to index 2  
nums[2] = 4 → go to index 4  
nums[4] = 2 → go to index 2  
nums[2] = 4 → index 4  
nums[4] = 2 → index 2  
...
Now you're stuck in a cycle: 2 → 4 → 2 → 4 → 2...

Let’s Draw This Graphically:
Each index is a node. Each nums[i] is a pointer:

0 → 1 → 3 → 2 ↘
        ↑     ↓
        ←---  4
You can now see a cycle: 2 → 4 → 2...

So this is just like a linked list with a cycle! And the entry point of the cycle is the duplicate value: 2.

Floyd’s algorithm works because:
You always reach the cycle due to the duplicate
slow and fast pointers must meet somewhere in the cycle
Then, you start a new pointer from the beginning
Where they meet next is the entry point of the cycle, i.e., the duplicate number

'''
class Solution:
    # Time: O(N)
    # Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        head = 0
        while True:
            slow = nums[slow]
            head = nums[head]
            if head == slow:
                return slow
              
