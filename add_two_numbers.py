# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Time: O(M+N)
    # Space: O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp = res = ListNode()
        carry = 0

        # Implement manual addition
        while l1 and l2:
            value = l1.val + l2.val + carry
            curr, carry = value % 10, value // 10
            temp.next = ListNode(curr)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        # If either number is larger than the other
        while l1:
            value = l1.val + carry
            curr, carry = value % 10, value // 10
            temp.next = ListNode(curr)
            temp = temp.next
            l1 = l1.next      
        while l2:
            value = l2.val + carry
            curr, carry = value % 10, value // 10
            temp.next = ListNode(curr)
            temp = temp.next
            l2 = l2.next
        
        # Add the carry finally if it exists
        if carry:
            temp.next = ListNode(carry)

        return res.next

'''
Above code can be shortened to:

while l1 or l2 or carry:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0

    # new digit
    val = v1 + v2 + carry
    carry = val // 10
    val = val % 10
    temp.next = ListNode(val)

    # update ptrs
    temp = temp.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

    return res.next
'''
        
