class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        group_list = [0] * (len(edges) + 1)
        for i in range(len(edges) + 1):
            group_list[i] = i
        for a, b in edges:
            a_root = self.find(a, group_list)
            b_root = self.find(b, group_list)
            if a_root == b_root:
                return [a,b]
            self.union(a_root, b_root, group_list)
  
    def union(self, root1, root2, group_list):
        group_list[root2] = root1
    
    def find(self, root, group_list):
        while root != group_list[root]:
            root = group_list[root]
        return root

        



        