# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(n) — one pass through the list.
    # Space: O(1) — no extra space used, reversal done in-place.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start from the first node, whose previous is None
        # Keep track of previous because that becomes the next of current node
        curr, prev = head, None
        # Till we reach the end, current node should now point to previous and current's next should point to current.
        # Then move previous and current forward for the next iteration.
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Previous is the last node of the list so that becomes the head now
        return prev

'''
Recursive solution takes same time but O(N) space due to recursion stack.

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head
  Node new_head = self.reverseList(head.next)
  head.next.next = head
  head.next = None
  return new_head
'''
