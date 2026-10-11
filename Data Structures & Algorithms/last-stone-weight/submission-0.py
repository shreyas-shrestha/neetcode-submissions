class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x > y:
                heapq.heappush_max(stones, x-y)
        if len(stones) == 0:
            return 0
        return heapq.heappop(stones)


        