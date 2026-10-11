class KthLargest:
    def __init__(self, k: int, nums:[]):
        nums.sort(reverse=True)
        self.nums = nums
        self.k = k
        self.heap = []
        i = 0
        while i < k and len(nums) > 0:
            heapq.heappush(self.heap, self.nums[i])
            i = i+1
            if i >= len(self.nums):
                break
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val) 
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]