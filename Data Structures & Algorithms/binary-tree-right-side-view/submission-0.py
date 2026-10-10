# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if root == None:
            return view
        self.rightHelper(root, 0, view)
        return view

    
    
    def rightHelper(self, root, level, view):
        if len(view) <= level:
            view.append(root.val)
        if root.right != None:
            self.rightHelper(root.right, level+1, view)
        if root.left != None:
            self.rightHelper(root.left, level+1, view)
        