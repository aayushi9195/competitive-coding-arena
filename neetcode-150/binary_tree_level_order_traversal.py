# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # Time: O(N) as we are touching every node once.
    # Space: O(N) as we are storing every node once in the queue.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If root is null, return empty list
        if not root:
            return []
        # Add root to start the process
        queue = deque()
        queue.append(root)
        res = []
        # We first get the length of the queue to know how many nodes belong to the current level. These nodes are popped and added to curr_level list.
        # And their non-empty children are added to the queue to be considered while traversing the next level.
        # Once we process all nodes as per the length of the queue initially found, we add the curr_level list to the final result.
        while queue:
            curr_level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr_level)
        return res            

        
