# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    

    # Similar to merge 2 lists.
    # We take 2 lists at a time, merge them and put them back. Continue this till we only have one list left. Similar to merge sort.
    # Time: O(nlogk)
    # Space: O(k)
    
    '''
    The merging is done in a pairwise manner (similar to a bottom-up merge sort). 
    In each iteration, the number of lists gets reduced approximately by half. 
    Initially, we have k lists, and we merge them in logk rounds.
    In each round, all nodes are processed at most once (since each merge operation is O(N)).
    The total number of nodes across all lists is N.
    Since the merging happens in O(N) time per level and there are O(logk) levels, the total time complexity is: O(Nlogk).

    At each iteration, we store merged linked lists in a temporary array merged_lists.
    This array holds about half the number of lists from the previous iteration.
    Initially, there are k lists. After merging once, there are k/2 lists, then k/4, and so on.
    The total storage required for merged_lists in each iteration is at most O(k).
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists
        return lists[0]

    # Since each node is processed exactly once, the time complexity is O(N), where N is the total number of nodes in the two lists being merged.
    def mergeTwoLists(self, l1, l2):
        dummy = head = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 or l2
        return head.next

              
