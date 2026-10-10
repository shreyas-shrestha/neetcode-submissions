# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_order = [[]]
        self.levelHelper(root, 0, level_order)
        return level_order
    
    def levelHelper(self, root, level, level_order) -> List[List[int]]:
        if len(level_order) <= level:
            start_level = []
            level_order.append(start_level)
            level_order[level].append(root.val)
        else:
            level_order[level].append(root.val)
        if root.left != None:
            self.levelHelper(root.left, level+1, level_order)
        if root.right != None:
            self.levelHelper(root.right, level+1, level_order)
        
        