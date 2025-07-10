# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(N)
    # Space: O(1)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        # Dummy node to handle edge case when left == 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 1. Move `prev` to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next

        # 2. Identify the start and end of the sublist
        start = prev.next           # This will become the tail of reversed sublist
        end = start
        for _ in range(right - left):
            end = end.next
        tail = end.next             # Node after the sublist

        # 3. Disconnect sublist and reverse it using existing logic of reverse linked list
        end.next = None             # Cut off the sublist
        reversed_head = self.reverseList(start)

        # 4. Reconnect reversed sublist with original list
        prev.next = reversed_head
        start.next = tail           # `start` is now at end of reversed sublist

        return dummy.next

    
    # Copied from previous reverse question
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


        

        
