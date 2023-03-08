# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
                   
                   
        if not root:
            return True     

        def dfs(root):
            if not root:
                return True

            left=dfs(root.left)
            right=dfs(root.right)
            if abs(left-right)>1:
                return -1
            if left==-1:
                return -1
            if right==-1:
                return -1            

            return 1+max(left,right)
            
        if dfs(root)==-1:
            return False
        return True
        


























        # def dfs(root):
        #     if not root:
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        #     return [balanced, 1 + max(left[1], right[1])]

        # return dfs(root)[0]