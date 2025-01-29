# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Time: O(N) as we touch every node once.
    # Space: O(N) due to recursion stack.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        # Swap the children to invert the current root.
        root.left, root.right = root.right, root.left

        # Invert the child nodes too at every level of the tree.
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Finally return the root, this will return intermediate roots from stack and finally return the main root once all recursion is done.
        return root
        
