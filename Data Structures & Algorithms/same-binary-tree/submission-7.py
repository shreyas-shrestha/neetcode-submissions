# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return self.recurse(p, q)
    
    def recurse(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = True
        right = True
        if p.val != q.val:
            return False
        if p.right is not None and q.right is not None:
            right = self.recurse(p.right, q.right)
        elif p.right is None and q.right is None:
            right = True
        else:
            return False
        if p.left is not None and q.left is not None:
            left = self.recurse(p.left, q.left)
        elif p.left is None and q.left is None:
            left = True
        else:
            return False
        if left == False or right == False:
            return False
        return True
            
        