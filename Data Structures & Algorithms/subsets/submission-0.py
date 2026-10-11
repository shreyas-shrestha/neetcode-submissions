class Solution:
    def subsets(self, nums: List[int]):
        to_return = []
        subset = []
        self.dfs(0, subset, nums, to_return)
        return to_return
    
    def dfs(self, index, subset, nums, to_return):
        if index >= len(nums):
            to_return.append(subset.copy())
            return
        subset.append(nums[index])
        self.dfs(index+1, subset, nums, to_return)
        subset.pop()
        self.dfs(index+1, subset, nums, to_return)




        



        