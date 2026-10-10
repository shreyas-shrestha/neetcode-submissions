class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = {}
        visited = set()
        ordering = []
        postorder = set()
        for prereq in prerequisites:
            adjacency_list.setdefault(prereq[1], []).append(prereq[0])
        for i in range(numCourses):
            adjacency_list.setdefault(i, [])
        for node in adjacency_list.keys():
            if node not in visited:
                temp = self.explore(node, ordering, visited, adjacency_list, postorder)
                if temp == []:
                    return []
        ordering.reverse()
        return ordering
    
    def explore(self, node, ordering, visited, adjacency_list, postorder):
        visited.add(node)
        for i in adjacency_list[node]:
            if i in visited and i not in postorder:
                return []
            if i not in visited:
                temp = self.explore(i, ordering, visited, adjacency_list, postorder)
                if temp == []:
                    return []
        ordering = ordering.append(node)
        postorder.add(node)
        return ordering

        