class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        order = []
        to_return = []
        for i, j in points:
            distance = i * i + j * j
            order.append((distance, (i,j)))
        heapq.heapify(order)
        for i in range(k):
            to_return.append(heapq.heappop(order)[1])
        return to_return


        