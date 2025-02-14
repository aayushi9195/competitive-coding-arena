# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Time: O(N^2) as we are calling a recursive function within another recursive function.
    # Space: O(N)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    ##### BETTER APPROACH #####

     # Time: O(N)
     # Space: O(H); best case O(logN) for balanced tree and worst case O(N) for degenerate tree
     def isBalancedOptimised(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            # Tracking height and balance-logic in the same iteration
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

        
