# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # keep track of longest path down and also longest length (left to right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        length, heights = self.length(root, 0, 0) # call length on root node
        return length
    
    def length(self, root: Optional[TreeNode], sideLength: int, height: int) -> (int, int):
        sideRight = 0 #longest diameter on right side
        sideLeft = 0 #longest diameter on left side
        heightLeft = 0 #longest path from NODE to down on left side
        heightRight = 0 #longest path from NODE to down on right side
        if root.right is not None:
            sideRight, heightRight = self.length(root.right, 0, 0)
            heightRight = heightRight + 1 #height is 0 at bottom and 1 as paths added bottom up
        if root.left is not None:
            sideLeft, heightLeft = self.length(root.left, 0, 0)
            heightLeft = heightLeft + 1
        height = max(heightLeft, heightRight) #height is the max counted bottom up of left and right
        sideLength = max(heightLeft + heightRight, sideLeft, sideRight) #longest side length is sidelength in left subtree, right subtree, or the heightleft + heightright
        return (sideLength, height)


        