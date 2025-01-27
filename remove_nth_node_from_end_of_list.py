# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(N)
    # Space: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast, slow = head, head

        # Move fast n times so distance between fast and slow becomes n.
        for i in range(n):
            fast = fast.next

        # This happens when n is same as size of the list, which means nth last node becomes the first node i.e. head.
        if not fast:
            return head.next

        # As distance between fast and slow is n, slow will point to the nth last node when fast reaches the end.
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth last node
        slow.next = slow.next.next

        # Finally return the head with removed node
        return head
        
