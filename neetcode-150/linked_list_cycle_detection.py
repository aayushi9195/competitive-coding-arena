# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Time: O(N)
    # Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast, slow = head, head

        # If there is a circle, and one pointer moves at 2x speed while the other moved at x speed, they will eventually catch up because as the distance between them keep increasing from one part of the circumference, it keeps reducing from the other part as it is a circle. 
        # If we reach the end of the list without the pointers meeting, it means there was no cycle. 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
        
