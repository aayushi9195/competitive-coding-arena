# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(H)
    # Space: O(H)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        if root.val > p.val and root.val < q.val:
            return root
        if root.val < p.val and root.val > q.val:
            return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

'''
Reduced lines of code with the same time/space complexity:

if not root or not p or not q:
    return None
if (max(p.val, q.val) < root.val):
    return self.lowestCommonAncestor(root.left, p, q)
elif (min(p.val, q.val) > root.val):
    return self.lowestCommonAncestor(root.right, p, q)
else:
    return root
'''
