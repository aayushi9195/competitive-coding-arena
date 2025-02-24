# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(N)
    # Space: O(N)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        # Inorder traversal while keeping a count of nodes
        def dfs(node):
            nonlocal cnt, res
            # Edge case
            if not node:
                return
            dfs(node.left)
            cnt -= 1
            # We have reached the kth largest element
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res
        
