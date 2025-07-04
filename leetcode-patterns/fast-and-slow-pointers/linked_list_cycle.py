# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(N)
    # Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast, slow = head, head
        # In a circle, if one pointer moves at x and other at 2x, distance between them keeps reducing by one each time, because the distance is increasing from one direction but decreasing from another due to the circle.
        # So keep moving at these speeds until a cycle is found or the faster pointer reaches the end of the list, which means there is no cycle.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

'''
Follow up question: Detect a cycle and if exists, find where it starts.

Let’s define some variables:
L = distance from head to cycle start
C = cycle length
X = distance from cycle start to the meeting point inside the loop

So:
Slow travels: L + X
Fast travels: L + X + nC (for some number of full cycles, n)
But fast moves twice as fast, so:
2(L + X) = L + X + nC

Solve the equation:
2L + 2X = L + X + nC
=> L + X = nC
=> L = nC - X
So if you start one pointer at head and one at the meeting point (X ahead in the cycle), and move both 1 step at a time, they'll meet at the start of the cycle (L steps away from head and C - X steps back from meeting point).

Pseudocode:
First meeting point proves a cycle exists (same as above).
Reset one pointer to head, move both at same speed.
They meet again at the start of the cycle.
'''
