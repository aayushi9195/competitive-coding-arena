# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Time: O(N) as DFS is applied on both trees simultaneously. Each node is visited once to compare its value and recursively check its left and right subtrees.
    # Space: O(logN) for a balanced tree, O(N) for a skewed tree. 
    # In a balanced tree, recursive calls only go as deep as log N before returning as that is the max height of the tree. The recursion doesn’t store all nodes at once—only one branch is fully stored at a time before unwinding.
    # In a skewed/degenerate tree, the height is N that is why recursion goes up to the last node and takes up O(N) space.
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        # At every step, the node in p and q should be same i.e. same value and same subtrees
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
