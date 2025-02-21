# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(N) as we are touching each node once.
    # Space: O(N) as we are storing each node in the queue.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        # Process nodes level by level.
        while queue:
            n = len(queue)
            # We are only interested in the rightmost node at every level.
            res.append(queue[-1].val)
            # Remove nodes at this level and push their left/right children to be considered for the next level.
            for i in range(n):
                node = queue.popleft() 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

        
