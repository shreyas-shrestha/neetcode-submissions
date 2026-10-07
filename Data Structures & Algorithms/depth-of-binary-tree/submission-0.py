# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.goDown(root, 1)
        
    
    def goDown(self, root: Optional[TreeNode], depth) -> int:
        left = 0
        right = 0
        if root.right is not None:
            right = self.goDown(root.right, depth + 1)
        if root.left is not None:
            left = self.goDown(root.left, depth + 1)
        if left == 0 and right == 0:
            return depth
        return max(left, right)
        

        