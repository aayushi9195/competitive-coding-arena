# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(N)
    # Space: O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        # Add 1 to account for current level.
        # Whichever subtree has more depth, consider that as final answer.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
