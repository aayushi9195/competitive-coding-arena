# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(N)
    # Space: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow, prev = head, head, None

        # find middle of the list
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # odd nodes - this makes sure the first half has (n/2) + 1 nodes
        if fast:
            prev = slow
            slow = slow.next
        
        # reverse second half
        slow = self.reverse(slow)

        # to keep the two halves separate i.e. head = 1, 2, 3 and slow = 5, 4 OR head = 1, 2 and slow = 4, 3
        prev.next = None

        # now take one node for each half and move to next i.e. merge two halves
        while head and slow:
            temp1 = head.next
            temp2 = slow.next
            head.next = slow
            slow.next = temp1
            head = temp1
            slow = temp2


    def reverse(self, node):
        curr, prev = node, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
