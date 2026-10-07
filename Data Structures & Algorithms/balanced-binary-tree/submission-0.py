# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        my_bool, height = self.height(root)
        return my_bool
    
    def height(self, root: Optional[TreeNode]) -> (bool, int):
        height_right = 0
        height_left = 0
        left_bool = True
        right_bool = True
        if root.right is not None:
            right_bool, height_right = self.height(root.right)
            height_right+=1
        if root.left is not None:
            left_bool, height_left = self.height(root.left)
            height_left+=1
        if abs(height_left - height_right) > 1 or left_bool == False or right_bool == False:
            return False, max(height_left, height_right)
        return True, max(height_left, height_right)

    