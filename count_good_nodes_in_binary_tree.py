# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(N)
    # Space: O(N)
    def goodNodes(self, root: TreeNode) -> int:

        # Can be done by BFS too
        def dfs(node, maxVal):
            # Check if node exists or not
            if not node:
                return 0
            # Check if this node is a good node
            res = 1 if node.val >= maxVal else 0
            # Update max value for next iterations
            maxVal = max(maxVal, node.val)
            # Count good nodes in left and right subtrees
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            # Return total count
            return res

        return dfs(root, root.val)
