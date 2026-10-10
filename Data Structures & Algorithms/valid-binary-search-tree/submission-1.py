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
                new_min = max(root.val, mini)
                right = self.validHelper(root.right, new_min, maxi)
        if root.left == None:
            left = True
        else:
            if root.left.val >= root.val:
                left = False
            else:
                new_max = min(root.val, maxi)
                left = self.validHelper(root.left, mini, new_max)
        return left and right
        

        