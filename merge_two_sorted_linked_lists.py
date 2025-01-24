# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Time: O(M+N)
    # Space: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Use dummy node to avoid handling edge cases separately
        temp = ListNode()
        result = temp

        # Keep picking the value that is smaller between list1 and list2.
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        # Below lines can be reduced to: temp.next = list1 or list2
        # This is because only either can be non null and or will give us the list that is not null
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        # Remember to exclude dummy node at the end.
        return result.next
