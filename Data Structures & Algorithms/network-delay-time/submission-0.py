class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_list = {}
        for start, end, time in times:
            if start not in adjacency_list:
                adj = []
                adj.append((end, time))
                adjacency_list[start] = adj
            else:
                adjacency_list[start].append((end, time))
        distance = {}
        for vertex in range(1, n+1):
            distance[vertex] = float('inf')
        distance[k] = 0
        priority_q = []
        heapq.heappush(priority_q, (0, k))
        while len(priority_q) > 0:
            curr_time, current = heapq.heappop(priority_q)
            if current not in adjacency_list or curr_time > distance[current]:
                continue
            for end, time in adjacency_list[current]:
                this_distance = curr_time + time
                if this_distance < distance[end]:
                    distance[end] = this_distance
                    heapq.heappush(priority_q, (this_distance, end))
        maximum_time = float("-inf")
        for dist in distance.values():
            if dist > maximum_time:
                maximum_time = dist
        if maximum_time == float('inf'):
            return -1
        return maximum_time

        
        