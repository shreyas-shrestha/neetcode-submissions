"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        marked = {}
        neighbors = []
        start = Node(node.val, None)
        marked[node] = start
        for i in node.neighbors:
            if i not in marked:
                neighbors.append(self.explore(i, marked))
            elif i in marked:
                neighbors.append(marked[i])
        start.neighbors = neighbors
        return start
 
    def explore(self, node: Optional['Node'], marked: dict):
        new_node = Node(node.val, None)
        marked[node] = new_node
        neighbors = []
        for i in node.neighbors:
            if i not in marked:
                neighbors.append(self.explore(i, marked))
            elif i in marked:
                neighbors.append(marked[i])
        new_node.neighbors = neighbors
        marked[node] = new_node
        return new_node 