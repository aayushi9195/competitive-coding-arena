# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(N)
# Space: O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        # If the list is empty or has only one node, we have nothing to swap
        if not head or not head.next:
            return head

        # Adding a dummy node so that the prev pointer can always point to the start of the next pair of nodes to be swapped
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        # While we have the next 2 nodes to be swapped
        while prev.next and prev.next.next:
           first = prev.next
           second = first.next
           rest = second.next

           # Swap 
           prev.next = second
           second.next = first
           first.next = rest

           # Move to the next pair
           prev = first

        # Return the real head
        return dummy.next

        
