# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        this_tree = self.sameTree(root, subRoot)
        right = False
        left = False
        if this_tree == True:
            return True
        if root.right != None:
            right = self.isSubtree(root.right, subRoot)
        if root.left != None:
            left = self.isSubtree(root.left, subRoot)
        return this_tree or right or left
  
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        left = False
        right = False
        if root.val == subRoot.val:
            if root.left != None and subRoot.left != None:
                left = self.sameTree(root.left, subRoot.left)
            if root.right != None and subRoot.right != None:
                right = self.sameTree(root.right, subRoot.right)
            if root.left == None and subRoot.left == None:
                left = True
            if root.right == None and subRoot.right == None:
                right = True
        if left == False or right == False:
            return False
        return True
        
        

        