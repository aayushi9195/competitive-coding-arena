# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(N)
    # Space: O(N)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # For every node check if it is valid and then check if both subtrees are also valid
        def isValid(node, minVal, maxVal):
            if not node:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            return isValid(node.left, minVal, node.val) and isValid(node.right, node.val, maxVal)
          
        # Use -float('inf') ad float('inf') if the range of node values is not known
        return isValid(root, -1001, 1001)
        
