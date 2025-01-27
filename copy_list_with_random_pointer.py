"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    # Time: O(N)
    # Space: O(N)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # We cannot simply iterate through the list and create copies of every node.
        # Because, while iterating through the list, when we encounter a node and create a copy of it, we can't immediately assign the random pointer's address. This is because the random pointer might point to a node that has not yet been created. To solve this, we can first create copies of all the nodes in one iteration.
        mapping = {None: None}
        temp = head
        while temp:
            mapping[temp] = Node(temp.val)
            temp = temp.next
        
        # Once we have all nodes copies, now we can focus on creating the next and random links.
        temp = head
        while temp:
            newNode = mapping[temp]
            newNode.next = mapping[temp.next]
            newNode.random = mapping.get(temp.random)
            temp = temp.next
        
        # Once both nodes and links are created, return the copy of head.
        return mapping[head]
        





        
