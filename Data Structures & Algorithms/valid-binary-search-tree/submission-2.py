# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validHelper(root, float('-inf'), float('inf'))
    
    def validHelper(self, root, mini, maxi) -> bool:
        left = False
        right = False
        if root.val >= maxi or root.val <= mini:
            return False
        if root.right == None:
            right = True
        else:
            if root.right.val <= root.val:
                right = False
            else:
                right = self.validHelper(root.right, root.val, maxi)
        if root.left == None:
            left = True
        else:
            if root.left.val >= root.val:
                left = False
            else:
                left = self.validHelper(root.left, mini, root.val)
        return left and right
        

        