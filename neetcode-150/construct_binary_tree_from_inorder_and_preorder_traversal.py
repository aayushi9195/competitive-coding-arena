# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Time: O(N)
    # Space: O(N)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # To make the lookups in inorder array faster
        mapping = {val : index for index, val in enumerate(inorder)}

        # Start from first node in preorder as that is the root of our tree
        self.pre_ind = 0

        def dfs(l, r):
            # It means all nodes are processed
            if l > r:
                return None
            # This is the root of the current subtree.
            root_val = preorder[self.pre_ind]
            self.pre_ind += 1
            root = TreeNode(root_val)
            # Find where does this root lie in inorder list. All nodes to the left of it will lie in the left subtree and all nodes to the right of it will lie in the right subtree.
            mid = mapping[root_val]
            # Repeat the process for both subtress. This time the inorder array to be considered will shrink based on which side of the root we are looking at.
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            # Once all subtrees are done, return the root.
            return root

        # Continue till all nodes in inorder list are processed
        return dfs(0, len(inorder) - 1)
        
