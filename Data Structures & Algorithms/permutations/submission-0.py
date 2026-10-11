class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        to_return = []
        subset = []
        for i in range(len(nums)):
            visited = set()
            self.backtrack(nums, subset, to_return, i, visited)
        return to_return
    
    def backtrack(self, nums, subset, to_return, index, visited):
        subset.append(nums[index])
        visited.add(index)
        if len(subset) == len(nums):
            to_return.append(subset.copy())
            visited.remove(index)
            subset.pop()
            return
        for i in range(len(nums)):
            if i not in visited:
                self.backtrack(nums, subset, to_return, i, visited)
        visited.remove(index)
        subset.pop()
        