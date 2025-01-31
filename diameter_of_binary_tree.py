# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Time: O(N)
    # Space: O(H) i.e. O(logN) for a balanced tree and O(N) for a skewed tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            # Refer to the shared variable inside a method
            nonlocal res
            # If the current node is empty, height from current node is 0
            if not root:
                return 0
            # Find the left and right heights
            left = dfs(root.left)
            right = dfs(root.right)
            # Diameter through this node is height of left subtree + height of right subtree
            res = max(res, left + right)
            # Height from current node
            return 1 + max(left, right)
        
        dfs(root)
        return res


        
        
