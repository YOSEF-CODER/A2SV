# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p is None or q is None:
            return None

        if root==p or root==q:
            return root

        if (root.left==p and root.right==q) and (root.left==q and root.right==p):
            return root

        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        return root