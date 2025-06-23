# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(M*N)
# Space: O(M+N)
class Solution: 
    # For every node in the main tree, we need to check if there is a complete match with subtree, so it takes no_of_roots in main tree * no_of_nodes in subtree time overall.
    # isSubTree calls recursion on the main tree, so it takes O(N) space. It parallely calls sameTree which takes O(M) space on the stack. As these calls are not nested, the overall space is O(M+N).
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        # Check if the trees match from this root
        if self.sameTree(root, subRoot):
            return True
        # If they don't then keep looking for a match in left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Returns true when two trees are exact copies of each other, false otherwise
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
